![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey?logo=linux)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

# 🛡️ Email Phishing Analyzer

A powerful CLI tool built for analyzing .eml email files (Gmail/Outlook exports) to detect phishing attacks, extract indicators of compromise (IOCs), perform basic OSINT, and generate reports.


## 🚀 Features

- 📩 Parses .eml email structure (From, To, Subject, Date, Body)
- 🕵️ Extracts:
  - URLs
  - IP Addresses
  - Emails
  - Hashes
- ⚠️ Detects phishing traits like:
  - Suspicious keywords
  - Generic greetings
- 🌍 OSINT enrichment of IPs using public APIs
- 📄 Exports results to PDF and CSV
- 🧪 Easily extendable modules for VirusTotal, attachments, etc.


## ⚙️ Requirements
- Python 3.8+
- Linux/macOS/WSL recommended

Install dependencies:

```bash
pip install -r requirements.txt

# Screenshots
analyzer.py.png 
'sample of results in reports folder.png' 
'tree -L 2.png'

#🧠 Usage
python3 analyzer.py
* Make sure the email sample is in: samples/test-phish.eml

# 📂 Project Structure

email-analyzer/
├── analyzer.py             # Main runner script
├── parser.py               # Email .eml parser
├── ioc_extractor.py        # Extracts IOCs from email
├── detectors.py            # Phishing detection logic
├── osint.py                # IP enrichment module
├── reporter.py             # PDF & CSV export
├── utils.py                # Utilities and helpers
├── samples/                # Test .eml files
│   └── test-phish.eml
├── results/                # Output folder (PDF/CSV)
├── requirements.txt
└── README.md

# 📊 Output Example

--- INDICATORS OF COMPROMISE ---
URLS: ['http://malicious-link.com/verify']
IPS: ['8.8.8.8']
EMAILS: ['alert@paypal.com']
HASHES: []

--- PHISHING DETECTION ---
[!] Suspicious Keywords Found: ['verify', 'urgent']
[!] Generic Greetings Found: ['dear user']

--- OSINT ENRICHMENT ---
{'IP': '8.8.8.8', 'City': 'Mountain View', 'Region': 'California', 'Country': 'US', 'Org': 'Google LLC'}

[+] Report saved to results/email_analysis.pdf
[+] IOCs saved to results/email_iocs.csv

# 🔮 Future Improvements
 • 🧪 Add VirusTotal lookup for URLs/Hashes
 • 📎 Scan attachments with ClamAV or VT
 • 📧 Integrate live email forwarding via IMAP
 • 🌐 Web dashboard (Flask or Streamlit)
 • 🧰 Docker packaging

# 👨‍💻 Author
Reinhard Amoah
EC-Council trained | Cybersecurity Enthusiast | Python Dev | Red Team
GitHub: @Reinhard1268 (https://github.com/Reinhard1268)


# ⚠️ Disclaimer
This tool is for educational and research purposes only. Do not use against systems or email accounts without explicit permission.
