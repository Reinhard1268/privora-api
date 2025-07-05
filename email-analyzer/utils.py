import os

def ensure_results_dir():
    if not os.path.exists("results"):
        os.makedirs("results")

def save_to_file(filename, content):
    ensure_results_dir()
    file_path = os.path.join("results", filename)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"[+] Saved to {file_path}")

def is_valid_email(email):
    import re
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None
