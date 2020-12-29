import requests
import time


def read_url(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(f"Response from url {url} is = {resp.status_code}")
    print(f"It took overall {time.time() - start} seconds")


if __name__ == "__main__":
    read_url(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
