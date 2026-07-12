import streamlit as st
import os

from resume_parser import extract_text
from analyzer import analyze_resume
from scorer import calculate_score

st.set_page_config(
    page_title="HireMind AI",
    page_icon="📄",   # or "🤖"
    layout="centered",
    initial_sidebar_state="collapsed"
)

# OPTIONAL EMAIL
from email_sender import send_email

UPLOAD_FOLDER = "resumes"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("Hire Mind AI")

# -----------------------------------
# FILE UPLOAD
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf", "docx", "jpg", "jpeg", "png"]
)

candidate_email = st.text_input("Candidate Email")

hr_email = st.text_input("HR Email")

# -----------------------------------
# BUTTON
# -----------------------------------

if st.button("Analyze Resume"):

    # CHECK FILE
    if uploaded_file is None:
        st.warning("Please upload a resume first.")
        st.stop()

    try:

        # SAVE FILE
        file_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("Resume Uploaded Successfully!")

        # -----------------------------------
        # EXTRACT TEXT
        # -----------------------------------

        text = extract_text(file_path)

        # DEBUG
        st.subheader("Extracted Resume Text")

        st.text(text[:1000])

        # -----------------------------------
        # ANALYZE
        # -----------------------------------

        analysis = analyze_resume(text)

        # -----------------------------------
        # SCORE
        # -----------------------------------

        score = calculate_score(analysis)

        # -----------------------------------
        # RESULTS
        # -----------------------------------

        st.subheader("Resume Analysis Results")

        st.write("Detected Skills:")
        st.write(analysis["skills"])

        st.write("Grammar Errors:")
        st.write(analysis["grammar_errors"])

        st.write("Projects Found:")
        st.write(analysis["projects"])

        st.write("Certifications Found:")
        st.write(analysis["certifications"])

        st.write("Resume Word Count:")
        st.write(analysis["length"])

        st.write("Final Resume Score:")
        st.write(score)
        # -----------------------------------
        # PERFORMANCE LEVEL
        # -----------------------------------

        if score >= 75:
            st.success("Excellent Resume")
        elif score >= 50:
            st.warning("⚠ Average Resume")
        else:
            st.error("❌ Candidate Rejected")

        # -----------------------------------
        # DECISION
        # -----------------------------------

        if score >= 70:

            st.success("✅ Candidate SHORTLISTED")

            st.balloons()

            # EMAILS OPTIONAL
            try:

                send_email(
                    candidate_email,
                    "Resume Shortlisted",
                    "Congratulations! You are shortlisted."
                )

                send_email(
                    hr_email,
                    "Candidate Shortlisted",
                    f"Candidate score is {score}"
                )

                st.success("Emails Sent Successfully!")

            except Exception as email_error:

                st.error(f"Email Error: {email_error}")

        else:

            st.error("❌ Candidate REJECTED")

            try:

                send_email(
                    candidate_email,
                    "Resume Rejected",
                    "Sorry! You are not shortlisted."
                )

            except Exception as email_error:

                st.error(f"Email Error: {email_error}")

    except Exception as e:

        st.error(f"System Error: {e}")
