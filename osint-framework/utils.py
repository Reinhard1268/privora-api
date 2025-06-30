import os
import re

def ensure_results_directory():
    if not os.path.exists("results"):
        os.makedirs("results")

def save_output(filename, content_lines):
    """Writes a list of strings to results/filename"""
    if not content_lines:
        print(f"[!] No data to write to {filename}")
        return

    output_path = os.path.join("results", filename)
    with open(output_path, "w") as f:
        if isinstance(content_lines, list):
            f.write("\n".join(content_lines))
        else:
            f.write(str(content_lines))
    print(f"[+] Saved to {output_path}")

def is_valid_email(email):
    """Basic email pattern checker"""
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(email_regex, email) is not None
