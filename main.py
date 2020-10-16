import sys

args = sys.argv
tasks = []

try:
    command = args[1]
except IndexError:
    print("Invalid arguments!")
    sys.exit(1)

if command not in ("add", "remove", "list"):
    print("Invalid command, Use add/remove/list")
    sys.exit(1)

if command == "add":
    title = args[2]
    content = args[3]
    task = title + content
    file = open("tasks.txt", "a")
    file.write(task+"\n")
    file.close()
elif command == "remove":
    print("removing")
elif command == "list":
    file = open("tasks.txt", "r")
    tasks = file.readlines()
    if len(tasks) == 0:
        print("No tasks present.")
    else:
        for task in tasks:
            title, content = task.split("|")
            print("{0} {1}".format(title, content))
    file.close()
else:
    print("invalid command!")
