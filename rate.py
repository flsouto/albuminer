from utils import *
from argparse import ArgumentParser
cli = SearchCLI.from_sys_args(
    lambda p : p.add_argument('rate', type=int)
)

meta = cli.meta()
albums = cli.albums()
current = meta['current']['key']
albums[current]['rate'] = cli.params.rate
albums.save()
print(albums[current])
