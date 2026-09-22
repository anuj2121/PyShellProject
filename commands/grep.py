def run(args):

    show_line_number = False

    if args[0] == "-n":
        show_line_number = True
        pattern = args[1]
        filename = args[2]
    else:
        pattern = args[0]
        filename = args[1]

    with open(filename, "r") as file:
        for i, line in enumerate(file, start=1):

            if pattern in line:

                if show_line_number:
                    print(
                        f"{filename}:{i}:{line.strip()}"
                    )

                else:
                    print(line.strip())