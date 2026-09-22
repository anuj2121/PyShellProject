import importlib
import shlex

PROMPT = "PyShell> "

while True:
    try:
        user_input = input(PROMPT).strip()

        if not user_input:
            continue

        parts = shlex.split(user_input)

        command = parts[0]
        args = parts[1:]

        try:
            module = importlib.import_module(
                f"commands.{command}"
            )

            module.run(args)

        except ModuleNotFoundError:
            print(f"`{command}` is an invalid command")

    except Exception as e:
        print(
            f"*** Unhandled `{type(e).__name__}` exception: {e}"
        )