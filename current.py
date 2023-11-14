from utils import *
cli = SearchCLI.from_sys_args()
current = cli.meta()['current']
key = current['key']
album = cli.albums()[key]
print(album)
