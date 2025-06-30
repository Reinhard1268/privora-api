import dns.resolver

def perform_dns_lookup(domain):
    output = f"[+] DNS Lookup for {domain}\n"
    output += "-" * 40 + "\n"

    try:
        a_records = dns.resolver.resolve(domain, 'A')
        output += "A Records:\n"
        for rdata in a_records:
            output += f" - {rdata.address}\n"
    except Exception as e:
        output += f"A Record Error: {e}\n"

    try:
        aaaa_records = dns.resolver.resolve(domain, 'AAAA')
        output += "\nAAAA Records:\n"
        for rdata in aaaa_records:
            output += f" - {rdata.address}\n"
    except Exception as e:
        output += f"\nAAAA Record Error: {e}\n"

    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        output += "\nMX Records:\n"
        for rdata in mx_records:
            output += f" - {rdata.preference} {rdata.exchange}\n"
    except Exception as e:
        output += f"\nMX Record Error: {e}\n"

    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        output += "\nNS Records:\n"
        for rdata in ns_records:
            output += f" - {rdata.target}\n"
    except Exception as e:
        output += f"\nNS Record Error: {e}\n"

    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        output += "\nTXT Records:\n"
        for rdata in txt_records:
            output += f" - {str(rdata.strings[0], 'utf-8')}\n"
    except Exception as e:
        output += f"\nTXT Record Error: {e}\n"

    return output
