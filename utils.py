import sys
from diskcache import Cache
from pathlib import Path
import httpx
from jsondb import Object

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

class SearchCLI:
    def __init__(self,dir):
        self.dir = dir

    def meta(self):
        return Object(Path(self.dir) / "metadata.json")

    def albums(self):
        return Object(Path(self.dir) / "albums.json")

    def from_sys_args():

        import argparse
        from pathlib import Path
        from utils import err

        p = argparse.ArgumentParser()
        p.add_argument("search_name")
        params = p.parse_args()
        dir = Path(__file__).with_name("data") / params.search_name
        meta_f = dir / "metadata.json"

        if not meta_f.exists():
            err("File not found: " + str(meta_f))

        return SearchCLI(dir)



