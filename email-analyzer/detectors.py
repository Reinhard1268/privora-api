import re

PHISHING_KEYWORDS = [
    "verify", "update", "login", "click here", "suspend",
    "confirm", "security alert", "unusual activity", "account locked"
]

GENERIC_GREETINGS = [
    "dear user", "dear customer", "valued customer"
]

def detect_phishing_keywords(text):
    found = []
    for word in PHISHING_KEYWORDS:
        if re.search(rf'\b{word}\b', text, re.IGNORECASE):
            found.append(word)
    return found

def detect_generic_greetings(text):
    found = []
    for phrase in GENERIC_GREETINGS:
        if phrase.lower() in text.lower():
            found.append(phrase)
    return found
