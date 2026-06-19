

import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai
import json


# GEMINI CONFIGURATION and used python libraries


genai.configure(
    api_key="GEMINI_API_KEY"
)

model = genai.GenerativeModel("gemini-2.5-flash")


# PAGE CONFIG


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# CUSTOM CSS implemetation

st.markdown("""
<style>

.main{
    background-color:#2563eb;
}

.title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
    color: #007399;
}

.subtitle{
    text-align:center;
    color:black;
    font-size:18px;
    margin-bottom:30px;
}


.card{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.skill{
    display:inline-block;
    background:#2563eb;
    color:white;
    padding:8px 15px;
    border-radius:20px;
    margin:5px;
    font-size:14px;
}

.good{
    color:green;
    font-weight:bold;
}

.bad{
    color:red;
    font-weight:bold;
}

.score{
    text-align:center;
    color:#2563eb;
    font-size:50px;
    font-weight:bold;
}
            
.stApp{
         background-color:white;
            }

</style>
""", unsafe_allow_html=True)


# HEADER Section

st.markdown("""
<div class="title">
AI Resume Analyzer
</div>

<div class="subtitle">
Upload your resume and get AI-powered ATS insights
</div>
""", unsafe_allow_html=True)


# ANALYZE FUNCTION Section

def analyze_resume(resume_text):

    prompt = f"""
    Analyze the following resume.

    Return ONLY JSON.

    {{
      "Candidate Name":"",
      "Email":"",
      "Skills":[],
      "Education":"",
      "Years of Experience":"",
      "ats_score":0,
      "summary":"",
      "strengths":[],
      "weaknesses":[]
    }}

    ATS score must be an integer between 0 and 100.

    Resume:
    {resume_text}
    """

    response = model.generate_content(prompt)

    return response.text


# FILE UPLOAD section

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("✅ Resume Uploaded Successfully")

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    with st.expander("View Extracted Resume Text"):
        st.text(text[:3000])

    
    # ANALYZE BUTTON
    

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            try:

                result = analyze_resume(text)

                result = result.replace("```json", "")
                result = result.replace("```", "")
                result = result.strip()

                data = json.loads(result)

                ats_score = str(data["ats_score"])

                digits = ''.join(filter(str.isdigit, ats_score))

                if digits:
                    score = int(digits[:3])
                else:
                    score = 0

               
                # REPORT TITLE
                

                st.header("Resume Analysis Report")

            
                # ATS SCORE CARD details 
                

                st.markdown(f"""
                <div class="card">
                    <h2>ATS Score</h2>
                    <div class="score">{score}/100</div>
                </div>
                """, unsafe_allow_html=True)

                st.progress(score / 100)

                
                # PROFILE CARD Details
               

                st.markdown(f"""
                <div class="card">
                    <h2>👤 Candidate Profile</h2>
                    <p><b>Name:</b> {data["Candidate Name"]}</p>
                    <p><b>Email:</b> {data["Email"]}</p>
                    <p><b>Education:</b> {data["Education"]}</p>
                    <p><b>Experience:</b> {data["Years of Experience"]}</p>
                </div>
                """, unsafe_allow_html=True)

                
                # SUMMARY details
                

                st.markdown(f"""
                <div class="card">
                    <h2>Professional Summary</h2>
                    <p>{data["summary"]}</p>
                </div>
                """, unsafe_allow_html=True)

                
                # SKILLS container
                

                skills_html = ""

                for skill in data["Skills"]:
                    skills_html += f'<span class="skill">{skill}</span>'

                st.markdown(f"""
                <div class="card">
                    <h2>Skills</h2>
                    {skills_html}
                </div>
                """, unsafe_allow_html=True)

                
                # STRENGTHS Details
            

                strengths_html = ""

                for strength in data["strengths"]:
                    strengths_html += f"<p class='good'>✔ {strength}</p>"

                st.markdown(f"""
                <div class="card">
                    <h2>Strengths</h2>
                    {strengths_html}
                </div>
                """, unsafe_allow_html=True)

                
                # WEAKNESSES
            
                weak_html = ""

                for weakness in data["weaknesses"]:
                    weak_html += f"<p class='bad'>{weakness}</p>"

                st.markdown(f"""
                <div class="card">
                    <h2>Weaknesses</h2>
                    {weak_html}
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:

                st.error("Error while analyzing resume")
                st.code(str(e))