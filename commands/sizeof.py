import os

def run(args):
    if not args:
        print("sizeof: filename required")
        return

    size = os.path.getsize(args[0])

    print(f"{size} bytes")