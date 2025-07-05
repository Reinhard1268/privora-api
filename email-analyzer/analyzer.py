from parser import parse_eml
from ioc_extractor import extract_iocs
from detectors import detect_phishing_keywords, detect_generic_greetings
from osint import enrich_ip
from reporter import export_to_pdf, export_to_csv
from utils import ensure_results_dir

# Set the file path
eml_file_path = "samples/test-phish.eml"

# Parse the email
email_data = parse_eml(eml_file_path)

if not email_data:
    print("[!] Email parsing failed. Exiting.")
    exit()

# Output email headers
print(f"From: {email_data['From']}")
print(f"To: {email_data['To']}")
print(f"Subject: {email_data['Subject']}")
print(f"Date: {email_data['Date']}")

# Output body
print("\n--- BODY ---\n")
print(email_data['Body'])

# Extract IOCs
print("\n--- INDICATORS OF COMPROMISE ---")
iocs = extract_iocs(email_data['Body'])
for key, value in iocs.items():
    print(f"{key.upper()}: {value}")

# Phishing Detection
print("\n--- PHISHING DETECTION ---")
keywords = detect_phishing_keywords(email_data['Body'])
greetings = detect_generic_greetings(email_data['Body'])
if keywords:
    print(f"[!] Suspicious Keywords Found: {keywords}")
if greetings:
    print(f"[!] Generic Greetings Found: {greetings}")
if not keywords and not greetings:
    print("[+] No obvious phishing indicators detected.")

# OSINT on IPs
print("\n--- OSINT ENRICHMENT ---")
for ip in iocs["ips"]:
    info = enrich_ip(ip)
    print(f"{ip}: {info}")

# Save results
ensure_results_dir()
export_to_pdf(email_data, iocs, keywords, greetings)
export_to_csv(email_data, iocs)

print("\n[✓] Analysis complete. Reports saved to /results.")
