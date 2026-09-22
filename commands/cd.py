import os

def run(args):
    print("ARGS:", args)

    if not args:
        return

    os.chdir(args[0])

    print("NOW:", os.getcwd())