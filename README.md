AI Resume Analyzer

AI Resume Analyzer is a Streamlit-based web application that uses Gemini AI to analyze resumes and provide ATS-friendly insights.

#Features

- Upload Resume in PDF format
- Extract resume text automatically
- ATS Score Calculation
- Candidate Profile Analysis
- Skills Extraction
- Professional Summary Generation
- Strengths Identification
- Weakness Detection
- Interactive Dashboard UI

# Technologies Used

- Python
- Streamlit
- Gemini AI
- PyPDF2
- HTML
- CSS

## 📦 Installation

1. Clone the repository

```bash
git clone <repository-url>
```

2. Navigate to the project folder

```bash
cd AI_Resume_Analyzer
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Add your Gemini API Key

Replace:

```python
api_key="YOUR_API_KEY"
```

with your own API key.

5. Run the application

```bash
streamlit run app.py
```

# How It Works

1. Upload a PDF resume.
2. Resume text is extracted using PyPDF2.
3. Gemini AI analyzes the content.
4. The system generates:
   - ATS Score
   - Skills
   - Summary
   - Strengths
   - Weaknesses
5. Results are displayed in a professional dashboard.
6. <img width="1581" height="1010" alt="Screenshot 2026-06-19 184242" src="https://github.com/user-attachments/assets/8ee321ae-4a34-4d08-9010-4475110dd75b" />

<img width="1677" height="786" alt="Screenshot 2026-06-19 184306" src="https://github.com/user-attachments/assets/02f960c5-0a32-421e-8d05-00f64a5f3039" />


<img width="1740" height="603" alt="Screenshot 2026-06-19 184319" src="https://github.com/user-attachments/assets/3df72109-6270-4d2f-93b2-36d915d10142" />


