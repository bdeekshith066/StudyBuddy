import streamlit as st
import streamlit.components.v1 as components

def app():
    gradient_text_html = """
        <style>
    .gradient-text {
        font-weight: bold;
        background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
        background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);


        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline;
        font-size: 3em;
    }
    </style>
    <div class="gradient-text">Welcome to Study Buddy </div>
    """

        # Render the gradient text
    st.markdown(gradient_text_html, unsafe_allow_html=True)
    
    st.write("Your Ultimate Study Companion for Enhanced Note-Taking, Comprehensive Exam Preparation, and Efficient PDF Management.")
    st.image('divider.png')
    st.markdown("##### Struggling to make notes directly in your PDFs? Craving a better learning experience? Wrestling with PDF handling and editing? Say goodbye to these challenges with Study Buddy! We have got the solution. With Study Buddy, streamline your study sessions, boost your productivity, and take control of your study materials effortlessly.  Check out the features below!")
    
    st.title('')

    col1, col2, col3 = st.columns([2.6,0.3,1])

    with col1:

        st.write("- <span style='font-size: larger;'><b>:orange[NotesCrafter]📝</b></span> - Upload your PDFs, select the page number, and craft personalized notes seamlessly with NotesCrafter, enhancing your study materials effortlessly.", unsafe_allow_html=True)
        st.write("- <span style='font-size: larger;'><b>:orange[PrepnMaster]👨‍🏫</b></span> - Master your exam preparation with quizzes, summaries, and an interactive chatbot. Customize your study method with any uploaded PDF.", unsafe_allow_html=True)
        st.write("- <span style='font-size: larger;'><b>:orange[MindMap]🧠</b></span> - Elevate your studying and revision with MindMapper – the ultimate tool for dynamic mind maps and diagrams.", unsafe_allow_html=True)
        st.write("- <span style='font-size: larger;'><b>:orange[StudyCircle]📖</b></span> - Collaborate in real-time with StudyCircle – share  code with friends, ask questions, and enhance your learning together.", unsafe_allow_html=True)
        st.write("- <span style='font-size: larger;'><b>:orange[PDFPro]📒</b></span> - Extract images, convert formats to PDF, merge, split, and take control of your PDF files with ease.", unsafe_allow_html=True)

    with col3:
        st.title('')
        st.write('')
        components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
  margin: 0; /* Remove default margin */
  padding: 0; /* Remove default padding */
}
body {
  font-family: Verdana, sans-serif;
}
.mySlides {
  display: none;
}
img {
  vertical-align: middle;
  width: 100%; /* Make images fill their containers */
  margin: 0; /* Remove any margin */
  padding: 0; /* Remove any padding */
}
/* Slideshow container */
.slideshow-container {
  max-width: 300px;
  max-height : 300px;
  position: 100%;
  margin: 0;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.2s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
</style>
</head>
<body>
<div class="slideshow-container">
  <div class="mySlides fade">
    <div class="numbertext">1 / 4</div>
    <img src="https://cdn.dribbble.com/users/1180873/screenshots/16502837/media/a555456b3f7d77276b70587f8afd93ea.png">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">2 / 4</div>
    <img src="https://assets-global.website-files.com/5aa7081220a301f2a3644f3b/6067a1648aaf24492c40f22f_shutterstock_1935177872.jpg">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRDmQbdccm-bRrC9Y4amLVY-yfWtJquFpf5g&s">
    
  </div>
  <div class="mySlides fade">
    <div class="numbertext">3 / 4</div>
    <img src="https://marketplace.canva.com/EAFipCHqmhY/1/0/1600w/canva-purple-colorful-organic-mind-map-brainstorm-gKBEZtdQsC0.jpg">
    
  </div>
</div>
<script>
  let slideIndex = 0;
  showSlides();

  function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}    
    slides[slideIndex-1].style.display = "block";  
    setTimeout(showSlides, 2000); // Change image every 2 seconds
  }
</script>
</body>
</html>
    """,
    height=200, width=300)
    
