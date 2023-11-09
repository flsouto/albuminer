import sys

def dd(var):
    print(var)
    exit()

def err(msg) :
    sys.stderr.write(msg + "\n")
    exit(1)
