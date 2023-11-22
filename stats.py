from utils import *

cli = SearchCLI.from_sys_args()

albums = cli.albums()

print('Total albums: %d' % len(albums.keys()))

total_rated = len([k for k in albums.keys() if 'rate' in albums[k]])
total_rated_up = len([k for k in albums.keys() if 'rate' in albums[k] and albums[k]['rate'] > 2  ])

print('Rated albums: %d' % total_rated)
print('Rated up: %d' % total_rated_up)
