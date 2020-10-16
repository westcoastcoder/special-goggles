import sys
# Convert the txt based file into one that uses sqlite3
import sqlite3

args = sys.argv
# print(type(args))

# Create connection to sqlite3 database
conn = sqlite3.connect("tasks.sqlite")

# Create cursor
cur = conn.cursor()

# Create our table if necessary
cur.executescript('''
CREATE TABLE IF NOT EXISTS TaskList (
    task_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT,
    content TEXT
);
''')

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
    try:
        file = open("tasks.txt", 'r')
    except IOError as e:
        print(str(e))
        sys.exit(1)
    file.close()
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    task_id = args[2]
    del tasks[int(task_id)]
    file = open("tasks.txt", "w")
    tasks = [task + "\n" for task in tasks]
    file.writelines(tasks)
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
