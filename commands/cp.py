import shutil

def run(args):
    if len(args) < 2:
        print("cp: source and destination required")
        return

    shutil.copy2(args[0], args[1])