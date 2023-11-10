import sys
from diskcache import Cache
from pathlib import Path
import httpx

def dd(var):
    print(var)
    exit()

def err(msg) :
    sys.stderr.write(msg + "\n")
    exit(1)

def GET(url):
    cache_path = Path(__file__).with_name("cache")
    cache = Cache(cache_path)
    content = cache.get(url)
    if not content :
        content = httpx.get(url).text
        cache.set(url, content, expire=300)
    return content
