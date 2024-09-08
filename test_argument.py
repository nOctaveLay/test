import argparse
parser = argparse.ArgumentParser(description = "Hello, World!")
parser.add_argument('-d','--documents')

if __name__ == "__main__":
    args = parser.parse_args('-d -1'.split())
    with open("test.md","w") as f:
        f.write(args.documents)