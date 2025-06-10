import argparse

##
# 1. Create the parser
parser = argparse.ArgumentParser(description="A simple greeting program.")

# 2. Add arguments
parser.add_argument("name", help="The name of the person to greet.")

# Optional Arguments
parser.add_argument("--polite", action="store_true",
                    help="Use a polite greeting.")

# Arguments with Values
parser.add_argument("--age", type=int, default=30,
                    help="The person's age (default: 30).")

# 3. Parse the arguments
args = parser.parse_args()

# 4. Use the arguments
if args.polite:
    print(f"Greetings, noble {args.name}!")
else:
    print(f"Hello, {args.name}!")

print(f"{args.name} is {args.age} years old.")
