import argparse

# Initialize parser
parser = argparse.ArgumentParser()
parser.add_argument("--number", help = "A number to print")

args = parser.parse_args()

print(args.number)

