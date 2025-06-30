import requests

def enumerate_subdomains(domain, wordlist_path="data/subdomains.txt"):
    found = []
    try:
        with open(wordlist_path, "r") as f:
            subdomains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[-] Subdomain wordlist not found.")
        return []

    print(f"[+] Enumerating subdomains for {domain}...")
    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            res = requests.get(url, timeout=2)
            if res.status_code:
                found.append(f"{sub}.{domain}")
        except requests.RequestException:
            continue
    return found
