# 🕵️ OSINT Recon Framework

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Tested%20on-Kali%20Linux-red?logo=linux)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Project%20Status-Active-brightgreen)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-blueviolet)


An advanced Open Source Intelligence (OSINT) tool built for red teamers, threat hunters, and cybersecurity analysts.  
This tool helps gather domain, IP, social, and breach data passively with modular recon functions.



## 🔍 Features

- ✅ WHOIS Lookup 
- ✅ DNS Enumeration 
- ✅ HTTP Headers Inspection
- ✅ Subdomain Enumeration
- ✅ Social Media Account Recon
- ✅ Breach Detection (Email-based, via HIBP)


## ⚙️ Usage

```bash
# Basic command
python3 main.py --target example.com --whois --dns

# Full sweep (domain)
python3 main.py --target example.com --whois --dns --headers --subdomains --social

# Email breach check
python3 main.py --email user@example.com


## 📦 Requirements

- Install all dependencies with:
pip install -r requirements.txt

## If you’re using .env for breach lookups:
HIBP_API_KEY=your_api_key_here


## 📁 Directory Structure

osint-framework/
├── main.py
├── modules/
├── utils.py
├── results/
├── data/
└── requirements.txt

## 🖼️ Screenshots
'all combined.png'            'EMAIL BREACH(mock).png'         'subdomains and results in cat.png'
'detecting invaid email.png'  'social and results in cat.png'  'tree of directory.png'


## 📛 Author

Reinhard Amoah
EC-Council Trained | Threat Hunter | Python Dev | Red Team
GitHub: Reinhard1268 (https://github.com/Reinhard1268)
