# HireMind AI - Intelligent Resume Screening System

## Overview

HireMind AI is an AI-powered Resume Screening System developed using Python and Streamlit. The application helps recruiters automate the resume screening process by extracting resume content, analyzing candidate profiles, assigning scores, and recommending whether candidates should be shortlisted.

---

## Features

- Upload resumes in PDF, DOCX, JPG, JPEG, and PNG formats
- OCR support for scanned/image resumes
- Automatic resume parsing
- Technical skill extraction
- Project detection
- Certification detection
- Education analysis
- CGPA evaluation
- Resume quality scoring
- Grammar estimation
- Keyword stuffing detection
- Candidate shortlisting
- Email notification support
- Interactive Streamlit dashboard

---

## AI Techniques Used

- Resume Parsing
- Optical Character Recognition (OCR)
- Rule-Based NLP
- Keyword Matching
- Resume Ranking Algorithm
- Automated Candidate Screening

---

## Tech Stack

- Python
- Streamlit
- PDFPlumber
- Python-docx
- OpenCV
- Tesseract OCR
- Pillow
- Pandas
- Scikit-learn
- Regex

---

## Project Structure

```
HireMind AI/
│
├── app.py
├── analyzer.py
├── resume_parser.py
├── scorer.py
├── email_sender.py
├── requirements.txt
├── resumes/
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/HireMind-AI.git
cd HireMind-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Install additional packages

```bash
pip install pytesseract pillow opencv-python language-tool-python
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

---

## Install Tesseract OCR

Download and install Tesseract OCR from:

https://github.com/UB-Mannheim/tesseract/wiki

Update the installation path in:

```python
resume_parser.py
```

Example

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Workflow

1. Upload Resume
2. Extract Resume Text
3. Analyze Skills
4. Detect Projects
5. Detect Certifications
6. Evaluate Education
7. Calculate Resume Score
8. Shortlist or Reject Candidate
9. Send Email Notification (Optional)

---

## Resume Evaluation Criteria

- Technical Skills
- Project Experience
- Certifications
- Education
- CGPA
- Resume Length
- Grammar Quality
- Keyword Stuffing

---

## Future Improvements

- BERT/Transformer-based Resume Parsing
- GPT-powered Resume Feedback
- ATS Compatibility Score
- Job Description Matching
- Semantic Skill Matching
- Experience Prediction
- Resume Ranking Dashboard
- Recruiter Analytics
- Database Integration
- Multi-language Resume Support

---

## Author

Developed by **Druva Kumar V**

Artificial Intelligence & Machine Learning Engineer