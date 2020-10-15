import sys
# print(sys.argv)

# for i, item in enumerate(sys. argv):
#    print("{0} {1}".format(i, item))

args = sys.argv
print(args)

try:
    command = args[1]
except IndexError:
    print("Invalid arguments!")
    sys.exit(1)

if command not in ("add", "remove", "list"):
    print("Invalid command, Use add/remove/list")

if command == "add":
    print("adding")
elif command == "remove":
    print("removing")
elif command == "list":
    print("listing")
else:
    print("invalid command!")
