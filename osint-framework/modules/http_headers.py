import requests

def grab_http_headers(domain):
    url = f"https://{domain}"
    headers_file = f"results/{domain}_headers.txt"

    try:
        response = requests.get(url, timeout=10)
        with open(headers_file, 'w') as f:
            f.write(f"[+] HTTP Headers for {domain}\n")
            f.write("-" * 40 + "\n")
            for key, value in response.headers.items():
                f.write(f"{key}: {value}\n")
        print(f"[+] Saved HTTP headers to {headers_file}")
    except requests.RequestException as e:
        print(f"[!] Error fetching headers for {domain}: {e}")
