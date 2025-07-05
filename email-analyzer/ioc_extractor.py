import re

def extract_iocs(text):
    iocs = {
        "urls": re.findall(r'(https?://[^\s]+)', text),
        "ips": re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text),
        "emails": re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text),
        "hashes": re.findall(r'\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{64}\b', text)
    }
    return iocs
