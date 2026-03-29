import streamlit as st
from resume_parser import extract_text
from model import predict_role, extract_skills, match_score
st.set_page_config(page_title="AI Resume Screener", layout="wide")

st.title("AI Resume Screener 🚀")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text(uploaded_file)

    # ✅ FIRST compute everything
    role, confidence = predict_role(text)
    skills = extract_skills(text)

    # ✅ THEN show UI
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Resume Preview")
        st.write(text[:500])

    with col2:
        st.subheader("Predicted Role")
        st.success(role)
        st.write(f"Confidence: {confidence:.2f}")

        st.subheader("Skills")
        st.write(skills)