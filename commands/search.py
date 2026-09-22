import os

def run(args):

    search_path = "."
    filename = None

    for arg in args:
        if arg.startswith("--in="):
            search_path = arg.split("=", 1)[1]

        elif arg.startswith("--file="):
            filename = arg.split("=", 1)[1]

    if not filename:
        print("search: filename required")
        return

    for root, dirs, files in os.walk(search_path):
        if filename in files:
            print(os.path.join(root, filename))