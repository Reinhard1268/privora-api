def perform_whois_lookup(domain):
    import whois
    import os
    from datetime import datetime

    w = whois.whois(domain)
    filename = f"results/{domain}_whois.txt"

    with open(filename, "w") as f:
        f.write(f"[+] WHOIS Lookup for {domain}\n")
        f.write("-" * 31 + "\n")
        f.write(f"Domain Name: {w.domain_name}\n")
        f.write(f"Registrar: {w.registrar}\n")
        f.write(f"Creation Date: {w.creation_date}\n")
        f.write(f"Expiration Date: {w.expiration_date}\n")
        f.write(f"Name Servers: {w.name_servers}\n")
        f.write(f"Emails: {w.emails}\n")

    print(f"[+] WHOIS results saved to {filename}")
