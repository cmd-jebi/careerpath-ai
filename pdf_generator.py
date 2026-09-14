# pdf_generator.py
from fpdf import FPDF

def create_pdf_report(scores, ai_text):
    pdf = FPDF()
    pdf.add_page()
    
    # Title
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "CareerPath AI - Senior High School Guidance Summary", ln=True, align="C")
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 5, "O*NET Interest Profiler (USDOL/ETA) - Adapted Exploratory Material", ln=True, align="C")
    pdf.ln(5)

    # RIASEC Scores Summary
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "Your RIASEC Interest Profile Scores:", ln=True)
    pdf.set_font("Helvetica", "", 10)
    for domain, score in scores.items():
        pdf.cell(0, 6, f"- {domain}: {score} / 10", ln=True)
    pdf.ln(5)

    # Recommendations Output
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 8, "AI Prediction & Skill Gap Analysis:", ln=True)
    pdf.set_font("Helvetica", "", 9)
    
    # Clean up markdown asterisks for plain PDF rendering
    clean_text = ai_text.replace("**", "").replace("#", "")
    pdf.multi_cell(0, 5, clean_text)
    
    # Mandatory Disclaimer Notice
    pdf.ln(5)
    pdf.set_font("Helvetica", "I", 8)
    pdf.multi_cell(0, 4, "Notice: This document is generated as an exploratory guidance report. It is not an officially binding DepEd track placement order. Please review these results with your designated Guidance Counselor.")

    return bytes(pdf.output())