import os
import requests
from dotenv import load_dotenv

load_dotenv()

print("🏁 Starting Bot")

url = requests.get(
    f"{os.getenv('CLOUDFLARE_KV_URL')}/python",
    headers={"Authorization": f"Bearer {os.getenv('CLOUDFLARE_KV_KEY')}"},
    timeout=10,
)

url = url.content.decode("utf-8")

print(url)
