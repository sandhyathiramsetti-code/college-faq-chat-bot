import requests
from pages import COLLEGES

headers = {"User-Agent": "Mozilla/5.0 (college-project-bot)"}

for key, college in COLLEGES.items():
    print(f"\n=== {college['name']} ===")
    for page in college["pages"]:
        try:
            r = requests.get(page["url"], headers=headers, timeout=10, allow_redirects=True)
            status = "OK" if r.status_code == 200 else f"WARN {r.status_code}"
        except requests.exceptions.RequestException as e:
            status = f"FAIL"
        print(f"  {status:<10} {page['label']:<35} {page['url']}")
