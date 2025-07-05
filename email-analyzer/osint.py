import geoip2.database
import os

# Load the GeoLite2-City.mmdb database
GEOIP_DB_PATH = "GeoLite2-City.mmdb"

def enrich_ip(ip_address):
    if not os.path.exists(GEOIP_DB_PATH):
        print(f"[!] GeoIP database not found at {GEOIP_DB_PATH}")
        return None

    try:
        reader = geoip2.database.Reader(GEOIP_DB_PATH)
        response = reader.city(ip_address)

        enriched_data = {
            "IP": ip_address,
            "City": response.city.name,
            "Region": response.subdivisions.most_specific.name,
            "Country": response.country.iso_code,
            "Org": "N/A"  # You can integrate ASN info here later
        }

        reader.close()
        return enriched_data

    except Exception as e:
        print(f"[!] Failed to enrich IP {ip_address}: {e}")
        return None
