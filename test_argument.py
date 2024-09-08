import argparse, os
parser = argparse.ArgumentParser(description = "Hello, World!")
parser.add_argument('-d','--documents')

if __name__ == "__main__":
    args = parser.parse_args()
    a = args.documents if args.documents is not None else "-1"
    os.system(f'echo {a}')
    b = a.split("/")
    os.system(f'echo {b}')
    # if args.documents is not None:
    #     with open("test.md","w") as f:
    #         f.write(args.documents)