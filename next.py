from utils import *
from argparse import ArgumentParser
from random import choice
from jsondb import Object

cli = SearchCLI.from_sys_args()
albums = cli.albums()

keys = [k for k in albums.keys() if not 'rating' in albums[k]]

if not keys: err('No more albums available')

key = choice(keys)

meta = cli.meta()

if 'current' in meta:
    meta['prev'] = meta['current']

meta['current'] = albums[key].copy()
meta['current']['key'] = key
meta.save()

print(albums[key]['url'])
