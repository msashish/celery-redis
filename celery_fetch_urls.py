import requests
from celery_config import app


@app.task
def fetch_url(url):
    resp = requests.get(url)
    print(f"Response from url {url} is = {resp.status_code}")


