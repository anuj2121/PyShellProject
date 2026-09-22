import importlib
import time

def run(args):

    cmd = args[0]
    cmd_args = args[1:]

    start = time.perf_counter()

    module = importlib.import_module(f"commands.{cmd}")
    module.run(cmd_args)

    end = time.perf_counter()

    print(
        f"`{' '.join(args)}` took "
        f"{end - start:.6f} seconds."
    )