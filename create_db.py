import sqlite3

conn = sqlite3.connect('todo-database.db')
# print("Opened database successfully")

# conn.execute('''CREATE TABLE TO_DO_USERS
#          (ID INTEGER PRIMARY KEY AUTOINCREMENT,
#          USERNAME TEXT NOT NULL,
#          PASSWORD TEXT NOT NULL,
#          EMAIL TEXT NOT NULL);''')
# print("Table created successfully")
# conn.close()

conn.execute('''CREATE TABLE "TO_DO_TASKS" (
	"TASK_ID"	INTEGER NOT NULL,
	"TASK_NAME"	TEXT NOT NULL,
	"USER_ID"	INTEGER NOT NULL,
	PRIMARY KEY("TASK_ID" AUTOINCREMENT),
	FOREIGN KEY("USER_ID") REFERENCES "TO_DO_USERS"("ID")
);''')
print("Table created successfully")
conn.close()