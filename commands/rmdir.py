import os

def run(args):
    if not args:
        print("rmdir: directory name required")
        return

    try:
        os.rmdir(args[0])
    except OSError:
        print(f"rmdir: `{args[0]}` is not empty.")