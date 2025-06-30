# modules/breach_check.py

def check_breach(email):
    # MOCK RESPONSE – Replace with actual API later
    mock_breaches = {
        "testaccount@gmail.com": [
            {"name": "Adobe", "date": "2013-10-04", "data": ["Emails", "Passwords"]},
            {"name": "LinkedIn", "date": "2012-05-05", "data": ["Emails", "Hashes"]}
        ]
    }

    return mock_breaches.get(email.lower(), [])
