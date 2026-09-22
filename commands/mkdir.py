import os

def run(args):
    if not args:
        print("mkdir: directory name required")
        return

    folder = args[0]

    if os.path.exists(folder):
        print(f"mkdir: `{folder}` already exists.")
        return

    os.mkdir(folder)