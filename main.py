
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide")

import home, notes, prepn,  mindmap, studycircle


    
        




# Reducing whitespace on the top of the page
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({
            "title": title,
            "function": func
        })   

    def run(self):  # Need to include self as the first parameter
        with st.sidebar:
            st.markdown("""
          <style>
            .gradient-text {
              margin-top: -20px;
            }
          </style>
        """, unsafe_allow_html=True)
            
            typing_animation = """
            <h3 style="text-align: left;">
            <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=35&Left=true&vLeft=true&width=500&height=70&lines=Study Buddy" alt="Typing Animation" />
            </h3>
            """
            st.markdown(typing_animation, unsafe_allow_html=True)
            
            app = option_menu(
                menu_title='Sections',
                options=['Home', 'NotesCrafter📝', 'PrepnMaster👨‍🏫','MindMapper🧠', 'StudyCircle📖' ],
                default_index=0,
            )
            
           
            st.sidebar.write("")
            linkedin_url = "https://www.linkedin.com/in/deekshith2912/"
            linkedin_link = f"[CodeIon]({linkedin_url})"
            st.sidebar.header(f"Developed  by {linkedin_link}")
            
        if app == "Home":
            home.app()
        
        elif app == 'NotesCrafter📝':
            notes.app() 
        elif app == 'PrepnMaster👨‍🏫':
            prepn.app()
        elif app == 'MindMapper🧠':
            mindmap.app()
        elif app == 'StudyCircle📖':
            studycircle.app()
            

# Create an instance of the MultiApp class and run the app
MultiApp().run()
