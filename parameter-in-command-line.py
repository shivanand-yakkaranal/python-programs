import sys
print(len(sys.argv))
if len(sys.argv) !=2:
    print("Usage: python read_file.py <filename>")
    sys.exit(1)

filename=sys.argv[1]
try:
    with open(filename,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print(f"Error: the {filename} doesn't exist")

