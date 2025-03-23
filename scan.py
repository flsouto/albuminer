from utils import *
from jsondb import Object
from bs4 import BeautifulSoup
import json
from bs4 import BeautifulSoup as bs
from slugify import slugify
from jsondb import Object
import time
from argparse import ArgumentParser

cli = SearchCLI.from_sys_args()
meta = cli.meta()
albums = cli.albums()
url = meta['search_url'].replace('advanced','ajax-advanced')
new_albums = 0

ap = ArgumentParser()
ap.add_argument('--start','-s',nargs='?',default=0,type=int)
ap.add_argument('--end','-e',nargs='?',default=10000,type=int)
ap.add_argument('--json','-j',nargs='?',default='',type=str)

params,_ = ap.parse_known_args()

def process_response(response):

    global albums, new_albums

    songs = response['aaData']

    if not songs: return

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
            albums[slug] = {"url": href_album}
            albums.save()
            print("New album slug: "+slug)
            print("Total new albums: "+str(new_albums))

if params.json:
    with open(params.json, "r", encoding="utf-8") as file:
        print(file)
        data = json.load(file)
        process_response(data)
else:

    for i in range(params.start, params.end, 200):

        print("Current index: "+str(i))
        url_paged = url.replace('songs?','songs?iDisplayStart=' + str(i) + '&')
        response = json.loads(GET(url_paged))
        print("Scanning " + url_paged)
        process_response(response)
        time.sleep(5)

print("Total new albums: "+str(new_albums))
