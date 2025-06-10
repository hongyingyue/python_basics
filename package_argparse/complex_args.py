import argparse

parser = argparse.ArgumentParser(description="A program demonstrating nargs and choices.")

parser.add_argument("files", nargs='+',
                    help="One or more files to process.")
parser.add_argument("--mode", choices=['read', 'write', 'append'], default='read',
                    help="Operation mode (default: read).")

args = parser.parse_args()

print(f"Processing files: {args.files}")
print(f"Using mode: {args.mode}")