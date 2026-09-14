# app.py
import streamlit as st
import google.generativeai as genai
from data import ONET_QUESTIONS, SHS_PATHWAYS
from pdf_generator import create_pdf_report

# Page Config for Mobile Responsiveness
st.set_page_config(page_title="CareerPath AI", page_icon="🎓", layout="centered")

# --- STEP 1: LAUNCH & CONSENT SCREEN ---
st.title("🎓 CareerPath AI: SHS Guidance Engine")
st.caption("O*NET Interest Profiler by USDOL/ETA used under developer license. Adapted for DepEd Senior High Track alignment.")

with st.expander("📄 Data Privacy Notice & Terms of Use", expanded=True):
    st.write("We collect Grade 10 marks and interest responses to provide exploratory guidance under RA 10173 (Data Privacy Act of 2012). Results are decision-support estimates and do not replace human counselors.")
    consent = st.checkbox("I agree to provide my academic and interest data for this guidance test.")

if not consent:
    st.info("Please accept the terms above to proceed.")
    st.stop()

# --- STEP 2: STUDENT ACADEMIC MARKS INPUT ---
st.header("1. Academic Marks (Grade 10)")
col1, col2 = st.columns(2)
with col1:
    math_grade = st.number_input("Math Grade", min_value=60, max_value=100, value=85)
    sci_grade = st.number_input("Science Grade", min_value=60, max_value=100, value=85)
with col2:
    eng_grade = st.number_input("English Grade", min_value=60, max_value=100, value=85)
    tle_grade = st.number_input("TLE / Shop Grade", min_value=60, max_value=100, value=88)

# --- STEP 3: 60-ITEM O*NET PROFILER (MOBILE ACCORDIONS) ---
st.header("2. O*NET Interest Profiler")
st.write("Check the activities you would enjoy doing.")

riasec_scores = {}
total_checked = 0

for domain, questions in ONET_QUESTIONS.items():
    with st.expander(f"📌 {domain} Activities"):
        score = 0
        for idx, q in enumerate(questions):
            if st.checkbox(q, key=f"{domain}_{idx}"):
                score += 1
                total_checked += 1
        riasec_scores[domain] = score

# --- STEP 4: LOW-ENGAGEMENT VALIDATOR ---
if total_checked == 0 or total_checked == 60:
    st.warning("⚠️ Response Check: You selected either 0 or all 60 items. Please re-evaluate your true preferences for an accurate prediction.")

# --- STEP 5: AI RECOMMENDATION ENGINE (GEMINI) ---
api_key = st.text_input("Enter Gemini API Key (Free):", type="password")

if st.button("Generate Career Pathway Recommendations") and api_key:
    if total_checked == 0 or total_checked == 60:
        st.error("Please provide realistic interest responses before generating recommendations.")
    else:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash')

        prompt = f"""
        Act as a Philippine High School Guidance Counselor. Analyze this Grade 10 student:
        - Subject Grades: Math: {math_grade}, Science: {sci_grade}, English: {eng_grade}, TLE: {tle_grade}
        - RIASEC Interest Profile Scores (out of 10): {riasec_scores}

        Provide a structured evaluation containing:
        1. Primary SHS Strand Recommendation (STEM, ABM, HUMSS, or TVL) with clear rationale.
        2. Academic Prerequisite Skill Gap Flags (Highlight subjects needing review before Grade 11).
        3. 2-3 Recommended College Degree Pathways & Stackable TESDA NC Certificates.
        Keep explanations concise, encouraging, and clear for a 16-year-old student.
        """

        with st.spinner("Analyzing profile and predicting career fit..."):
            response = model.generate_content(prompt)
            st.success("Analysis Complete!")
            st.markdown(response.text)

            # Store in session state for PDF generation
            st.session_state['result_text'] = response.text
            st.session_state['scores'] = riasec_scores

# --- STEP 6: PDF EXPORT BUTTON ---
if 'result_text' in st.session_state:
    pdf_bytes = create_pdf_report(st.session_state['scores'], st.session_state['result_text'])
    st.download_button(
        label="📥 Download Full Guidance Summary (PDF)",
        data=pdf_bytes,
        file_name="CareerPath_AI_Guidance_Report.pdf",
        mime="application/pdf"
    )
