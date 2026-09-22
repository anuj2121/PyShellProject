import os
import shutil

def run(args):
    if not args:
        print("rm: filename required")
        return

    try:
        if args[0] == "-r":
            shutil.rmtree(args[1])
            print(f"Removed directory {args[1]}")
        else:
            os.remove(args[0])
            print(f"Removed file {args[0]}")

    except FileNotFoundError:
        print("rm: file or directory not found")

    except PermissionError:
        print("rm: permission denied")

    except Exception as e:
        print(f"rm: {e}")