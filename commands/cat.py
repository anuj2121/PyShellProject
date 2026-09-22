def run(args):
    if not args:
        print("cat: filename required")
        return

    with open(args[0], "r") as file:
        print(file.read(), end="")