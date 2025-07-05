from fpdf import FPDF
import csv
import os

def export_to_pdf(email_data, iocs, keywords=None, greetings=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Email Phishing Analysis Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"From: {email_data['From']}", ln=True)
    pdf.cell(200, 10, txt=f"To: {email_data['To']}", ln=True)
    pdf.cell(200, 10, txt=f"Subject: {email_data['Subject']}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {email_data['Date']}", ln=True)

    pdf.ln(10)
    pdf.multi_cell(0, 10, txt="Body:\n" + email_data["Body"])

    pdf.ln(10)
    pdf.cell(200, 10, txt="Indicators of Compromise:", ln=True)
    for key, values in iocs.items():
        pdf.multi_cell(0, 10, f"{key.upper()}: {', '.join(values) if values else 'None'}")

    pdf.ln(10)
    pdf.cell(200, 10, txt="Phishing Detection:", ln=True)
    if keywords:
        pdf.multi_cell(0, 10, f"Suspicious Keywords: {', '.join(keywords)}")
    if greetings:
        pdf.multi_cell(0, 10, f"Generic Greetings: {', '.join(greetings)}")
    if not keywords and not greetings:
        pdf.multi_cell(0, 10, "No phishing indicators detected.")

    os.makedirs("results", exist_ok=True)
    pdf.output("results/report.pdf")

def export_to_csv(email_data, iocs, keywords=None, greetings=None):
    os.makedirs("results", exist_ok=True)
    with open("results/report.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Field", "Value"])
        writer.writerow(["From", email_data["From"]])
        writer.writerow(["To", email_data["To"]])
        writer.writerow(["Subject", email_data["Subject"]])
        writer.writerow(["Date", email_data["Date"]])
        writer.writerow([])
        writer.writerow(["Body", email_data["Body"]])

        writer.writerow([])
        writer.writerow(["Indicators of Compromise"])
        for key, values in iocs.items():
            writer.writerow([key.upper(), ", ".join(values) if values else "None"])

        writer.writerow([])
        writer.writerow(["Phishing Detection"])
        writer.writerow(["Suspicious Keywords", ", ".join(keywords) if keywords else "None"])
        writer.writerow(["Generic Greetings", ", ".join(greetings) if greetings else "None"])
