import requests

def check_social_media_profiles(username):
    platforms = {
        "Twitter (X)": f"https://x.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
    }

    results = {}
    for platform, url in platforms.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                results[platform] = url
            else:
                results[platform] = None
        except requests.RequestException:
            results[platform] = None

    return results
