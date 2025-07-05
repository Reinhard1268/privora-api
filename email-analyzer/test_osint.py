from osint import enrich_ip

ip = "8.8.8.8"
result = enrich_ip(ip)
if result:
    print(result)
else:
    print("Enrichment failed.")
