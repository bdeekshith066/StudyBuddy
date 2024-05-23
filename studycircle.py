import streamlit as st

def app():
    st.title("StudyCircle")
    st.write("Collaborate in real-time with StudyCircle – share code with friends, ask questions, and enhance your learning together.")

    st.image('divider.png')


    st.header('')

    st.write('')

    st.write("Are you tired of juggling multiple WhatsApp groups for different subjects or study groups? Do you often find yourself with numerous questions and doubts, longing to discuss and study with your friends in real-time? Look no further! With StudyCircle, you can collaborate seamlessly with your peers, share code, ask questions, and work together to enhance your learning experience. Simply enter a unique code or share the URL of the page, and voila! You have your own dedicated study space where you can engage in productive discussions, clarify doubts, and collectively elevate your academic journey.")

    st.title('')
    col1, col2, col3 = st.columns([0.3,1,0.5])

    
    with col2:
        input_text = st.text_input("Enter code:", max_chars=50)
        submitted = st.button("Submit")

    if submitted:
        if input_text:
            link = f"https://copying-theta.vercel.app/{input_text}"
            st.markdown(f"[Click here]({link}) to open the link.")
        else:
            st.error("Please enter some text.")

if __name__ == "__main__":
    app()
