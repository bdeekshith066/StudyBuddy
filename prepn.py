import streamlit as st
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
import pickle
import io
import os
import asyncio

# Replace with your actual OpenAI API key
api_key = ""

async def store_doc_embeddings(file, filename):
    reader = PdfReader(file)
    corpus = ''.join([p.extract_text() for p in reader.pages if p.extract_text()])
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(corpus)
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectors = FAISS.from_texts(chunks, embeddings)
    with open(filename + ".pkl", "wb") as f:
        pickle.dump(vectors, f)

async def get_doc_embeddings(file, filename):
    if not os.path.isfile(filename + ".pkl"):
        await store_doc_embeddings(file, filename)
    with open(filename + ".pkl", "rb") as f:
        vectors = pickle.load(f)
    return vectors

async def generate_quiz(num_questions, qa_chain):
    questions = []
    for _ in range(num_questions):
        question = "Generate a quiz question from the document."
        answer = await conversational_chat(question, qa_chain)
        questions.append((question, answer))
    return questions

async def generate_summary(num_words, qa_chain):
    query = f"Summarize the document in {num_words} words."
    summary = await conversational_chat(query, qa_chain)
    return summary

async def generate_important_points(num_points, qa_chain):
    query = f"List the top {num_points} important points from the document."
    points = await conversational_chat(query, qa_chain)
    return points

async def conversational_chat(query, qa_chain):
    result = qa_chain({"question": query, "chat_history": st.session_state['history']})
    st.session_state['history'].append((query, result["answer"]))
    return result["answer"]

def app():
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'ready' not in st.session_state:
        st.session_state['ready'] = False
    if 'generated' not in st.session_state:
        st.session_state['generated'] = ["Welcome! You can now ask any questions regarding the document."]
    if 'past' not in st.session_state:
        st.session_state['past'] = ["Hey!"]

    st.title("PDF Study Master")

    uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

    if uploaded_file is not None:
        with st.spinner("Processing..."):
            uploaded_file.seek(0)
            file = uploaded_file.read()
            vectors = asyncio.run(get_doc_embeddings(io.BytesIO(file), uploaded_file.name))
            qa_chain = ConversationalRetrievalChain.from_llm(
                ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=api_key), 
                retriever=vectors.as_retriever(), 
                return_source_documents=True
            )
        st.session_state['ready'] = True

    if st.session_state['ready']:
        st.header("Select Study Mode")
        study_mode = st.radio("Choose a study mode:", ["Quiz", "Summary", "Important Points", "Custom"])

        if study_mode == "Quiz":
            num_questions = st.number_input("Number of Questions", min_value=1, max_value=100, value=10)
            prompt = f"Hi! I want {num_questions} questions and answers for the document."
        elif study_mode == "Summary":
            num_words = st.number_input("Number of Words", min_value=10, max_value=1000, value=100)
            prompt = f"Hi! I want a summary in {num_words} words."
        elif study_mode == "Important Points":
            num_points = st.number_input("Number of Points", min_value=1, max_value=50, value=5)
            prompt = f"Hi! I want {num_points} important points for revision."
        else:
            prompt = st.text_input("Enter your custom prompt:")

        if st.button("Submit"):
            if study_mode == "Quiz":
                questions = asyncio.run(generate_quiz(num_questions, qa_chain))
                for idx, (question, answer) in enumerate(questions):
                    st.write(f"**Question {idx + 1}:** {question}")
                    st.write(f"**Answer:** {answer}")
            elif study_mode == "Summary":
                summary = asyncio.run(generate_summary(num_words, qa_chain))
                st.write("**Summary:**")
                st.write(summary)
            elif study_mode == "Important Points":
                points = asyncio.run(generate_important_points(num_points, qa_chain))
                st.write("**Important Points:**")
                st.write(points)
            else:
                output = asyncio.run(conversational_chat(prompt, qa_chain))
                st.write(output)

        

if __name__ == "__main__":
    app()
