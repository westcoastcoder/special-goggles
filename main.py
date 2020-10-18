import sys
# Convert the txt based file into one that uses sqlite3
import sqlite3

# Create connection to sqlite3 database
conn = sqlite3.connect("tasks.sqlite", isolation_level=None)
# Create cursor
cur = conn.cursor()

# Create our table if necessary
cur.execute('''
CREATE TABLE IF NOT EXISTS Tasklist (
    task_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT NOT NULL,
    content TEXT NOT NULL)
''')

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
    # Adds the new task to the database
    addSQL = '''INSERT INTO Tasklist (title, content) VALUES (?, ?)'''
    cur.execute(addSQL, (title, content))
    # Close connection to db
    conn.close()
elif command == "remove":
    # Fetch tasklist data from db
    fetchSQL = '''SELECT * FROM Tasklist'''
    cur.execute(fetchSQL)

    # Assign data to list
    fullTask = cur.fetchall()
    task_id = args[2]

    # This might explode if the list is empty
    try:
        del fullTask[int(task_id)-1]
    except IndexError as e:
        print('Error: ' + str(e))
        sys.exit(1)

    # Clear the db and reset autoincrement
    cur.execute('''DELETE FROM Tasklist;''',)
    cur.execute('''DELETE FROM sqlite_sequence WHERE NAME='Tasklist';''')

    # Re-pop the db with post-deletion task list
    for item in fullTask:
        cur.execute('''INSERT INTO Tasklist(title, content) VALUES (?, ?)''',
                    (item[1], item[2]))
    # Close connection to db
    conn.close()
elif command == "list":
    # get data from db
    fetchSQL = '''SELECT * FROM Tasklist'''
    cur.execute(fetchSQL)
    # Assign data to list
    fullTask = cur.fetchall()
    if len(fullTask) == 0:
        print("No tasks present.")
    else:
        print("|-{0}---{1}------{2}--------------|".format("index", "title", "content"))
        for i in range(len(fullTask)):
            title, content = fullTask[i][1], fullTask[i][2]
            print("|---{0}-----{1}----{2}--------------|".format(i, title, content))
    # Close connection to db
    conn.close()
else:
    print("invalid command!")
