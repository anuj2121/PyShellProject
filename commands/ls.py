import os

def run(args):
    path = "."

    if args:
        path = args[0]

    items = os.listdir(path)

    print(" ".join(items))