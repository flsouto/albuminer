from utils import *
from argparse import ArgumentParser
from random import choice
cli = SearchCLI.from_sys_args()
albums = cli.albums()
print(albums.keys())


