import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def check_email_breaches(email):
    # Simulated breach data (replace with real API later)
    known_breaches = {
        "testaccount@gmail.com": [
            {"site": "Adobe", "date": "2013-10-04", "data": "Emails, Passwords"},
            {"site": "LinkedIn", "date": "2012-05-05", "data": "Emails, Hashes"},
        ],
        "legituser@gmail.com": [
            {"site": "MySpace", "date": "2016-05-31", "data": "Emails, Passwords"},
        ]
    }

    return known_breaches.get(email, [])
