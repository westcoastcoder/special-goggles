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
    task = title + "|" + content
    file = open("tasks.txt", "a")
    file.write(task+"\n")
    file.close()
elif command == "remove":
    print("removing")
elif command == "list":
    try:
        file = open("tasks.txt", "r")
    except IOError as e:
        print(str(e))
        sys.exit(1)
    tasks = file.readlines()
    if len(tasks) == 0:
        print("No tasks present.")
    else:
        print("|-{0}---{1}------{2}----|".format("index", "title", "content"))
        tasks = [task.strip() for task in tasks]
        for i in range(len(tasks)):
            title, content = tasks[i].split("|")
            print("|-{0}--{1}----{2}-|".format(i, title, content))
    file.close()
else:
    print("invalid command!")
