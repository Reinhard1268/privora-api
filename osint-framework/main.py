import os
import argparse
from utils import save_output, ensure_results_directory, is_valid_email
from modules.whois_lookup import perform_whois_lookup
from modules.dns_lookup import perform_dns_lookup
from modules.http_headers import grab_http_headers
from modules.subdomain_enum import enumerate_subdomains
from modules.social_check import check_social_media_profiles
from modules.email_breaches import check_email_breaches

def main():
    parser = argparse.ArgumentParser(description="OSINT Recon Framework")
    parser.add_argument("--target", help="Domain or username to investigate")
    parser.add_argument("--email", help="Check if email has been in any breaches")
    parser.add_argument("--whois", action="store_true", help="Perform WHOIS lookup")
    parser.add_argument("--dns", action="store_true", help="Perform DNS lookup")
    parser.add_argument("--headers", action="store_true", help="Grab HTTP headers")
    parser.add_argument("--subdomains", action="store_true", help="Enumerate subdomains")
    parser.add_argument("--social", action="store_true", help="Search for social media accounts")
    args = parser.parse_args()

    ensure_results_directory()

    if args.email:
        if not is_valid_email(args.email):
            print(f"[!] Invalid email address: {args.email}")
            return
        breach_data = check_email_breaches(args.email)
        if breach_data:
            save_output(f"{args.email}_breaches.txt", breach_data)
        else:
            print("[-] No breach data found or API error.")
        return

    if not args.target:
        print("[!] Please provide a target using --target")
        return

    if args.whois:
        whois_data = perform_whois_lookup(args.target)
        if whois_data:
            save_output(f"{args.target}_whois.txt", whois_data)

    if args.dns:
        dns_data = perform_dns_lookup(args.target)
        if dns_data:
            save_output(f"{args.target}_dns.txt", dns_data)

    if args.headers:
        headers_data = grab_http_headers(args.target)
        if headers_data:
            save_output(f"{args.target}_headers.txt", headers_data)

    if args.subdomains:
        subdomains = enumerate_subdomains(args.target)
        if subdomains:
            subdomain_lines = [
                f"[+] Subdomains for {args.target}",
                "-" * 40
            ] + subdomains
            save_output(f"{args.target}_subdomains.txt", subdomain_lines)
        else:
            print("[-] No subdomains found.")

    if args.social:
        profiles = check_social_media_profiles(args.target)
        if profiles:
            save_output(f"{args.target}_social.txt", profiles)
        else:
            print("[-] No social profiles found.")

if __name__ == "__main__":
    main()
