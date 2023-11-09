import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--search_url', '-u')
parser.add_argument('--search_name', '-n')
params = parser.parse_args()

search_url = params.search_url or input('Search URL: ')
search_name = params.search_name or input('Search Name: ');

import json, os, slugify
from jsondb import Object

s_folder = os.path.join("data",  slugify.slugify(search_name))
os.makedirs(s_folder, exist_ok=True)

metadata = Object(os.path.join(s_folder, "metadata.json"))
metadata['search_name'] = search_name
metadata['search_url'] = search_url
metadata.save()
