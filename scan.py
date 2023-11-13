from utils import *
from jsondb import Object
from bs4 import BeautifulSoup
import json
from bs4 import BeautifulSoup as bs
from slugify import slugify
from jsondb import Object
import time

cli = SearchCLI.from_sys_args()
meta = cli.meta()
albums = cli.albums()
url = meta['search_url'].replace('advanced','ajax-advanced')
new_albums = 0

for i in range(0,10000,200):

    url_paged = url.replace('songs?','songs?iDisplayStart=' + str(i) + '&')
    print("Scanning " + url_paged)
    response = json.loads(GET(url_paged))
    songs = response['aaData']

    if not songs: break

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
    time.sleep(5)

print("Total new albums: "+str(new_albums))
