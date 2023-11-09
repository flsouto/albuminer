import sys
from diskcache import Cache
from pathlib import Path
import requests

def dd(var):
    print(var)
    exit()

def err(msg) :
    sys.stderr.write(msg + "\n")
    exit(1)

def get(url):
    cache_path = Path(__file__).with_name("cache")
    if not cache_path.is_dir() :
        cache_path.mkdir()
    cache = Cache(cache_path)
    content = cache.get(url)
    if not content :
        content = requests.get(url).text
        cache.set(url, content, expire=300)
    return content
