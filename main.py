import sys

args = sys.argv

try:
    command = args[1]
except IndexError:
    print("Invalid arguments!")
    sys.exit(1)

if command not in ("add", "remove", "list"):
    print("Invalid command, Use add/remove/list")
    sys.exit(1)

if command == "add":
    print("adding")
elif command == "remove":
    print("removing")
elif command == "list":
    print("listing")
else:
    print("invalid command!")
