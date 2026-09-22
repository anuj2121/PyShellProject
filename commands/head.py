def run(args):

    lines = 10
    filename = args[0]

    if args[0].startswith("-"):
        lines = int(args[0][1:])
        filename = args[1]

    with open(filename, "r") as file:
        for line in file.readlines()[:lines]:
            print(line.rstrip())