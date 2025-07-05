from email import policy
from email.parser import BytesParser

def parse_eml(file_path):
    try:
        with open(file_path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        # Handle both plain and multipart emails
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body = part.get_payload(decode=True).decode(errors='replace')
                    break
            else:
                body = "[!] No plain text body found in multipart email."
        else:
            body = msg.get_payload(decode=True)
            body = body.decode(errors='replace') if body else "[!] Empty body."

        return {
            "From": msg.get("From", "N/A"),
            "To": msg.get("To", "N/A"),
            "Subject": msg.get("Subject", "N/A"),
            "Date": msg.get("Date", "N/A"),
            "Body": body.strip()
        }

    except Exception as e:
        print(f"[!] Error parsing email: {e}")
        return None
