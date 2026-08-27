import sys


def hexdump(path: str, length: int = -1, show_path: bool = 0):

    try:
        with open(path, "rb") as file:

            if show_path: print(" " * 10 + f'Path: {path}\n')
            print(" " * 10 + " ".join([f'{i:X}'.zfill(2) for i in range(16)]) + "\n")

            if length < 0:
                file.read()
                length = file.tell()
                file.seek(0)

            for row in range(length // 16):
                bin_cut = file.read(16)
                #print(f"{file.tell()}", file=sys.stderr) - Author:  Hr. Thiel
                print(f"{
                    f"{row * 16:X}".strip().zfill(8)
                }  {
                    " ".join(
                        [ f"{char:X}".zfill(2) for char in bin_cut ]
                    ).rjust(39)
                }  {
                    "".join(char if ord(char) not in [i for i in range(32)] + [128] else "." for char in bin_cut.decode("utf-8"))
                }")

    except FileNotFoundError:
        print(f'File not found: "{path}"')


if __name__ == "__main__":
    if len(sys.argv) < 2 or any(map(lambda x: x in sys.argv, ["-h", "--help"])):
        print("Usage: python hexdump.py [PATH] [LENGTH]")

    else:
        hexdump(sys.argv[1])