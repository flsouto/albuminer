import argparse
from utils import *
from pathlib import Path
import sys
from jsondb import Object

p = argparse.ArgumentParser()
p.add_argument("search_name")
params = p.parse_args()

meta_f = Path(__file__).with_name("data") / params.search_name / "metadata.json"

if not meta_f.exists():
    err("File not found: " + str(meta_f))

meta = Object(meta_f)
dd(meta['search_url'])