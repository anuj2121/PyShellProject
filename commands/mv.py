import shutil

def run(args):
    if len(args) < 2:
        print("mv: source and destination required")
        return

    shutil.move(args[0], args[1])