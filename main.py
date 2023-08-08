import os
import requests
from dotenv import load_dotenv

load_dotenv()

print("🏁 Starting Bot")

url = requests.get(
    f"{os.getenv('CLOUDFLARE_KV_URL')}/values/python",
    headers={"Authorization": f"Bearer {os.getenv('CLOUDFLARE_KV_KEY')}"},
    timeout=10,
)
url = url.content.decode("utf-8")

metadata = requests.get(
    f"{os.getenv('CLOUDFLARE_KV_URL')}/metadata/python",
    headers={"Authorization": f"Bearer {os.getenv('CLOUDFLARE_KV_KEY')}"},
    timeout=10,
)
metadata = metadata.json()

mastodon_post = requests.post(
    "https://botsin.space/api/v1/statuses",
    headers={
        "Authorization": f"Bearer {os.getenv('MASTODON_ACCESS_TOKEN')}",
        "Content-Type": "application/x-www-form-urlencoded",
    },
    timeout=30,
    data={
        "status": f"{metadata['result']['author_name']}/"
        + f"{metadata['result']['repo_name']}"
        + f" - ⭐ {metadata['result']['total_stars']}"
        + f"\n{url}"
    },
)
mastodon_post.raise_for_status()


print("✅ Successfully posted to Mastodon")
