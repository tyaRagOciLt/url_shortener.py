# Python code for URL Shortener
import uuid

class URLShortener:
    def __init__(self):
        self.url_map = {}
    
    def shorten_url(self, url):
        uid = str(uuid.uuid4())[:6]
        shortened_url = f"http://short.url/{uid}"
        self.url_map[shortened_url] = url
        return shortened_url
    
    def redirect_url(self, short_url):
        return self.url_map.get(short_url, "URL not found.")

url_shortener = URLShortener()
short_url = url_shortener.shorten_url("https://www.google.com/")
print(short_url)
print(url_shortener.redirect_url(short_url))
