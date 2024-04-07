import sqlite3

# Create or open a database 
# Create or read a table using cursor objects  
# Read data using SELECT
# Add data to the table using INSERT 
# Modify data using UPDATE 
# Delete data using DELETE

class DBManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()
    
    def create_table_task(self):
        create_table = """CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name STRING NOT NULL, 
        priority INTEGER NOT NULL
        )"""

    def find_task(self, task_name, task_id=None):
        self.cursor.execute("SELECT * from MYTABLE where name = ?", (task_name,))
        return self.cursor.fetchone()

    def show_tasks(self):
        self.cursor.execute("SELECT * from MYTABLE")
        for row in self.cursor:
            print(row)
        
    def change_priority(self):
        task_id = int(input(f"Enter the id of the task: ")) 
        priority = 0
        while priority < 1:
            priority = int(input("Enter priority of the task: "))
        
        if not self.find_task(id=task_id):
            self.cursor.execute("UPDATE tasks SET prioiry = ? where id = ?", (priority, task_id))
