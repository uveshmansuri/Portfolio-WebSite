import streamlit as st
import google.generativeai as genai

api_key=st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash-lite")

st.set_page_config(
    page_title="Uvesh Mansuri | Portfolio",
    layout="wide",
    initial_sidebar_state="auto"
)

col1, col2 = st.columns([2 ,1])
with col1:
    st.markdown("## Hi :wave:")
    st.markdown("# I am Uvesh Mansuri")
    st.markdown("#### Flutter Developer | Android Developer | Tech Enthusiast ")
    st.write(
        """
         I'm Uvesh Mansuri. I'm currently pursuing an MCA at Manipal University Jaipur, studying online. 
         My passion lies in becoming a skilled Flutter and Android developer, and I'm constantly diving deeper into the exciting worlds of Artificial Intelligence and Machine Learning, especially in Computer Vision.
         I'm completed my Bachelor of Computer Applications (BCA) at Narmada College of Science & Commerce also Before that, I completed my 12th grade in Science (PCM) from GNFC Narmada Vidyalaya.
         \nMy main aspiration is to build impactful and intelligent applications that can make a real difference. 
         I'm particularly interested in using technology for education, automating processes with AI, and improving administrative
         systems for institutions like colleges and schools.I'm actively looking for opportunities to contribute my technical skills and grow as a developer.
        """
    )
with col2:
    st.image("Images/usm12.png")
st.divider()

persona = """
You are Uvesh Mansuri AI bot.
You help the people answer questions about yourself (i.e. Uvesh Mansuri)
Answer as if you are Uvesh speaking directly (use "I", "me", "my", etc.).
If you don’t know the answer or someone ask about private details, simply say: "That's a secret."
However, if someone asks unnecessary or abusive questions, respond politely but firmly. 
Do not say "That's a secret" in those cases—handle them appropriately with respect and confidence and you can talk strict tone as well.
Here is More info about Uvesh:

Full Name: Uvesh Salim Mansuri
Date of Birth: 07-Sep-2004
Address: Sheth Faliya Vadadla, Bharuch, Gujarat, India, 302015
Current Role: MCA Student at Manipal University Jaipur (Online Mode) | 
Aspiring Flutter & Android Developer and Passionate for Learning AI & ML and Computer Vision

Education:
Currently Pursuing an MCA at Manipal University Jaipur (Online Mode)
BCA (2022-2025), Narmada College of Science & Commerce (CGPA: 8.67/10) (Completed: Feb-2025)
12th Science – PCM, GNFC Narmada Vidyalaya (Completed: March-2022) (Pr: 54%)

🎯 Goals & Aspirations
Uvesh Mansuri is a passionate and driven computer science undergraduate, 
aspiring to become a mobile app developer with expertise in Flutter, 
Python, and full-stack application development. 
He aims to build impactful, smart applications with real-world utility, especially in the domains of education, AI-based automation, and administration systems of Institutions & Organizations specially in Teaching like Collages and Schools. 
He is actively seeking internships or full-time opportunities where he can contribute technically and grow asa developer.

💼 Skills & Technical Proficiency
Languages: Dart, Python, Java, PHP, C, C++, JavaScript, VB.NET
Frameworks/Platforms: Flutter, Android SDK, ASP.NET
Databases: Firebase (Realtime DB, Auth), MySQL, SQLite
Tools: VS Code, Android Studio, PyCharm, Git, GitHub
APIs & Services: REST APIs, FCM, Firebase Auth, Gemini API
Python & AI: OpenCV, face_recognition, NumPy, Pandas, YOLOv8, Deep Learning, Vector Embeddings
Soft Skills: Problem-solving, leadership, teamwork

💡 Key Projects
🚀 NCSC College App:
Tech Stack: Flutter, Firebase, Python (OpenCV, face_recognition), Gemini API
A comprehensive cross-platform application for college administration with AI automation, role-based access, and advanced attendance systems.
Access Control: Dynamic roles for students, staff, and administrators ensure secure access to tailored modules.
Academic Tools: Internal marks, attendance analytics, assignment tracking, and announcement dashboards.
AI-Driven Automation: Auto-generates timetables and test questions using intelligent models.
Face Recognition Attendance: Python-based system for live, secure attendance verification.
Request Automation & Library Management: Simplifies document submissions, fines, and issue/return tracking.
NCSC Project Documentation link 'https://drive.google.com/file/d/1Gp53We7U4ZBFpeifZ9aUbPOyETy_FGBU/view'

🗒️ Notify – Smart Note Assistant App (In Development):
Tech Stack: Flutter, Firebase, Gemini API, Vector Embeddings
An intelligent notes app that uses AI to enhance productivity through contextual assistance and chatbot interaction.
Features an AI assistant that suggests edits, categorizes notes, and retrieves content via natural language.
Built on vector embeddings for personalized note handling and smart reminder setting using Gemini Vector Embeddings Model.

📚 Coding Hub – Learning App for Android:
Tech Stack: Android SDK (Java, XML), Firebase, Gemini API, News API
An Android study companion for IT learners with dynamic quizzes and a Stack Overflow-style peer forum.
Generates topic-based quizzes and question papers using Gemini AI and enables group learning through discussion boards.
Integrates real-time tech news with save/bookmark functionality.
Coding Hub APK Link 'https://uveshmansuri.github.io/Coding-Hub-Web/downloadlink.html'

🧠 Liveness Checking Model:
Tech Stack: Python, OpenCV, YOLOv8n
A security-focused model that detects liveness in real-time using webcam input to prevent spoofing in facial detection.
Trained on over 4750 images using YOLOv5 to classify live vs. fake faces.
Combines cvzone and OpenCV for real-time detection and liveness checking.
Git Repo of model: "https://github.com/uveshmansuri/Liveness-Check.git"
Model Download Link: "https://drive.google.com/file/d/1gtc6ST5g9FKkT8hr6yaQ-ewUHmng7isP/view?usp=sharing"

🌟 Personality Traits
Builder Mindset: Enjoys solving real-world problems through smart application design with AI Powerd Features
Fast Learner: Continuously self-learning and experimenting with new tech (e.g., AI APIs)
Collaborative: Works well in teams and independently—shows leadership initiative in major projects
Detail-Oriented: Balances backend logic with UI/UX sensibility in cross-platform apps


Uvesh's Email: uveshmansuri794@gmail.com
Uvesh's GitHub: "https://github.com/uveshmansuri
Uvesh's LinkedIn: "https://linkedin.com/in/uvesh-mansuri-87164625b"
"""


st.title("🤖 My AI Bot")
user_question = st.text_input("Ask about me", key="question_input")
if st.button("Ask", use_container_width=True):
    if user_question.strip() == "":
        st.warning("Please enter a question before clicking 'Ask'.")
    else:
        prompt = persona + " Here is the question that the user asked: " + user_question
        response = model.generate_content(prompt)
        st.write(response.text)
        st.session_state.question_input = ""


#Sills Section
def colored_bar(label, value, color):
    st.markdown(f"""
    <div style="margin-bottom:10px;">
        <strong>{label}</strong>
        <div style="background-color: #e0e0e0; border-radius: 5px; height: 10px; width: 100%;">
            <div style="background-color: {color}; width: {value}%; height: 100%; border-radius: 5px;"></div>
        </div>
        <p>{value}%</p>
    </div>
    """, unsafe_allow_html=True)

def skill_bar(label, value, color):
    st.markdown(f"""
    <div style='margin-bottom: 10px;'>
        <b>{label}</b>
        <div style='background-color: #ddd; border-radius: 5px; height: 10px;'>
            <div style='width: {value}%; background-color: {color}; height: 100%; border-radius: 5px;'></div>
        </div>
        <small>{value}%</small>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Key Skills
st.header("🧰 Key Skills")
cols = st.columns(2)
with cols[0]:
    skill_bar("Flutter Dev", 90, "#4CAF50")
    skill_bar("Android App Dev", 90, "#2196F3")
    skill_bar(".NET", 70, "#9C27B0")
with cols[1]:
    skill_bar("Python", 85, "#FF9800")
    skill_bar("Computer Vision", 60, "#FF00F0")
    skill_bar("AI and ML", 50, "#F44336")

# Technical Skills Table
st.subheader("📊 Technical Skills")
with st.container():
    st.markdown("""
    <table style='width:100%;'>
        <tr><th align='left'>Programming Languages</th><td>Python, Java, Dart, JavaScript, C, C++, PHP, VB.NET, HTML & CSS</td></tr>
        <tr><th align='left'>Frameworks & Libraries</th><td>Android SDK, Flutter, YOLO, OpenCV, face_recognition, .NET</td></tr>
        <tr><th align='left'>Technologies</th><td>WordPress (Basic), Firebase Auth, FCM, REST APIs</td></tr>
        <tr><th align='left'>AI & Machine Learning</th><td>Gemini API, Vector Embeddings, Computer Vision, Data Visualization</td></tr>
        <tr><th align='left'>Tools & Platforms</th><td>Git, GitHub, Colab, VS Code, Android Studio</td></tr>
        <tr><th align='left'>Python Libraries</th><td>NumPy, Pandas, Matplotlib, CV2, torch, mediapipe, Flask, FastAPI</td></tr>
        <tr><th align='left'>Soft Skills</th><td>Problem Solving, Leadership, Teamwork</td></tr>
    </table>
    """, unsafe_allow_html=True)


st.divider()

#Projects
def project_card(title, desc, tech, bullets, git_repo=None, git_text=None, link=None, leading=None, link_text=None):
    git_html = f"<p><b><a href='{git_repo}' target='_blank'>{git_text}</a></b></p>" if git_repo and git_text else "<p></p>"
    link_html = f"<p><b>{leading}</b> <a href='{link}' target='_blank'><b>{link_text}</b></a></p>" if link and link_text else " "
    st.markdown(f"""
    <div style='background-color:#fff; padding:20px; border-radius:10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px;'>
        <h4>{title}</h4>
        <p>{desc}</p>
        <ul>{"".join(f"<li>{item}</li>" for item in bullets)}</ul>
        <p><b>Tech:</b> {tech}</p>
        {git_html}
        {link_html}
    </div>
    """, unsafe_allow_html=True)

with st.container():
    st.header("🗃️ MY Projects")
    project_card(
        "🚀 NCSC College App",
        "Cross-platform app using Flutter with face recognition attendance and AI-powered automation.",
        "Flutter, Firebase, OpenCV, face_recognition",
        [
            "Role-based access (admin, faculty, student, etc...)",
            "Real-time face recognition attendance"
            "Auto test generation, timetable with Gemini API",
            "Internal marks, attendance analytics, assignment tracking, and announcement dashboards"
        ],
        link="https://drive.google.com/file/d/1Gp53We7U4ZBFpeifZ9aUbPOyETy_FGBU/view?usp=sharing",
        leading="📄",
        link_text="Documentation",
    )

    project_card(
        "🗒️ Notify – Smart Note Assistant App (Under Development)",
        "Note-taking app with embedded chatbot and smart reminders.",
        "Flutter, Firebase, Gemini API",
        [
            "Chatbot for quick queries",
            "Vector embeddings for training Chatbot"
        ]
    )

    project_card(
        "📚 Coding Hub – Learning App for Android",
        "AI quiz, discussion forum & tech news in one learning platform.",
        "Android SDK, Firebase, Gemini API, News API",
        [
            "An Android study companion for IT learners",
            "Generates topic - based quizzes and question papers using Gemini AI",
            "Enables group learning through Stack Overflow-style peer forum",
            "Daily tech news via News API",
        ],
        link="https://uveshmansuri.github.io/Coding-Hub-Web/downloadlink.html",
        leading="📥",
        link_text="Download APK",
    )

    project_card(
        "🧠 Liveness Checking Model",
        "YOLO-based real-time spoof detection with webcam.",
        "Python, YOLO, OpenCV, Deep Learning",
        [
            "Face liveness classification",
            "Trained on 4750+ real/fake images"
        ],
        "https://github.com/uveshmansuri/Liveness-Check.git",
        "Instructions",
        "https://drive.google.com/file/d/1gtc6ST5g9FKkT8hr6yaQ-ewUHmng7isP/view?usp=sharing",
        "📥",
        "Download Model",
    )

# Contact Section
st.divider()

def contectcard(url,img_link,text):
    st.markdown(f"""
    <a href="{url}" target="_blank">
            <img src="{img_link}" 
                 alt="{text}" height="30" width="30"/>
        </a>
    """,unsafe_allow_html=True)

st.header("📇 Contact Me")
with st.container():
    col1,col2,col3 = st.columns([1,2,1])
    with col1:
        st.empty()
    with col2:
        st.markdown("#### 🏠 Sheth Faliya, Vadadla, Bharuch, Gujarat, 302015")
    with col3:
        st.empty()

    # Create 3 columns for social links
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.empty()

    with col2:
        contectcard(
            "mailto:uveshmansuri794@gmail.com",
            "https://img.icons8.com/color/48/000000/gmail--v1.png",
            "Email",
        )

    with col3:
        contectcard(
            "https://github.com/uveshmansuri",
            "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg",
            "GitHub",
        )

    with col4:
        contectcard(
            "https://www.linkedin.com/in/uvesh-mansuri-87164625b",
            "https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg",
            "LinkedIn"
        )

    with col5:
        st.empty()