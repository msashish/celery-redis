from celery_fetch_urls import fetch_url


def read_url(urls):
    for url in urls:
        fetch_url.delay(url)


if __name__ == "__main__":
    read_url(["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"])
