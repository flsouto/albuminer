import argparse
from utils import *
from pathlib import Path
import sys
from jsondb import Object
from bs4 import BeautifulSoup
import json

p = argparse.ArgumentParser()
p.add_argument("search_name")
params = p.parse_args()

meta_f = Path(__file__).with_name("data") / params.search_name / "metadata.json"

if not meta_f.exists():
    err("File not found: " + str(meta_f))

meta = Object(meta_f)
url = meta['search_url'].replace('advanced','ajax-advanced')

response = json.loads(GET(url))
songs = response['aaData']

from bs4 import BeautifulSoup as bs
from slugify import slugify
from jsondb import Object
albums = Object(meta_f.with_name('albums.json'))
new_albums = 0

for link_band,link_album,type,song,genre,*_ in songs:
    link_band = bs(link_band,'html.parser').a
    link_album = bs(link_album,'html.parser').a
    href_band = link_band.get('href')
    href_album = link_album.get('href')
    name_band = link_band.text
    name_album = link_album.text
    slug = slugify(name_band + " " + name_album)
    if not slug in albums:
        new_albums += 1
        print("New albums: "+str(new_albums))
    albums[slug] = {"url": href_album}

albums.save()
