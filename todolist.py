import os 
import mysql.connector
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
passs = os.getenv("my_sql_key")

def connectDB():
    connection=mysql.connector.connect(host='localhost',user='root',password=passs,database='finaltdl')
    return connection

# print("successfully connected")
# def initDB():
#     connection = connectDB()
#     cursor = connection.cursor()
#     cursor.execute('''
#         ALTER TABLE todos ADD COLUMN status VARCHAR(30) NOT NULL
#     ''')
#     connection.commit()
#     connection.close()
#     print('Column added successfully')

# def initDB():
#     connection=connectDB()
#     cursor=connection.cursor()
#     cursor.execute('''
#                    CREATE TABLE IF NOT EXISTS todos(
#                         id INT(15) PRIMARY KEY AUTO_INCREMENT,
#                         task varchar(255) NOT NULL,
#                         date DATE NOT NULL 
#                    )
#                    ''')
#     connection.commit()
#     connection.close()
#     print('TABLE created successfully')

# initDB()

def showtasks():
    connection = connectDB()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM todos")
    tasks = cursor.fetchall()

    if not tasks:
        print("YOUR TO-DO LIST IS EMPTY")
    else:
        print("\nTo-Do List:")
        print("-" * 40)
        for task in tasks:
            print(f"ID: {task[0]} | Task: {task[1]} | Due Date: {task[2]} | Task status : {task[3]}")
        print("-" * 40)

    connection.close()


# showtasks()

def create_tasks():
    connection= connectDB()
    cursor=connection.cursor()
    task=input("enter the task  :")
    date= input("enter the due date YYYY-MM-DD  : ")
    status=input("enter the task status :")
    query = 'INSERT INTO todos (task, date, status) VALUES (%s, %s, %s)'
    cursor.execute(query, (task, date, status,))  
    connection.commit()
    connection.close()
    print(f"Task '{task}'created successfully. ")

# create_tasks()

def check_status():
    connection = connectDB()
    cursor = connection.cursor()
    task_id = int(input("Enter the task ID to check status: "))

    query4 = 'SELECT status FROM todos WHERE id = %s'
    cursor.execute(query4, (task_id,))
    result = cursor.fetchone()

    if result:
        print(f"Task ID {task_id} Status: {result[0]}")
    else:
        print("No task found with the given ID.")

    connection.close()




def deletetask():
    connection = connectDB()
    cursor  = connection.cursor()
    task_id=int(input("ENTER THE TASK ID FOR DELETION : "))
    query1='DELETE FROM todos WHERE id = %s '
    cursor.execute(query1,(task_id,))
    connection.commit()
    connection.close()
    print(f"post for the task id = {task_id} has been deleted successfully.")

    
# deletetask()

def delete_all_tasks():
    connection = connectDB()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM todos")  # Deletes all records
    connection.commit()
    connection.close()
    print("All tasks have been deleted successfully.")


def update_tasks_by_id():
    connection=connectDB()
    cursor= connection.cursor()
    task_id=int(input("enter the task id you want to update : "))
    task=input("enter the updated task details :  ")
    date=input("enter the date in yyyy-mm-dd : ")
    query3 = 'UPDATE todos SET task = %s, date = %s WHERE id = %s'
    cursor.execute(query3, (task, date, task_id))  
    connection.commit()
    connection.close()
    print(f"Task ID {task_id} updated successfully.")

    
    # if not tasks:
    #     print("YOUR TO DO LIST IS EMPTY")
    # else:
    #     for index,task in enumerate(tasks):
    #         print(task)

# update_tasks_by_id()

def menu():
    while True:
        print("\nSelect an operation to perform:")
        print("1. Create Task")
        print("2. Show Task")
        print("3. Update Task")
        print("4. Delete single Task")
        print("5. status checker ")
        print("6. delete all tasks")
        print("7. to exit ")
        
        operation = input("Enter the operation to perform: ").strip()
        
        if operation == "1":
            create_tasks()
        elif operation == "2":
            showtasks()
        elif operation == "3":
            update_tasks_by_id()
        elif operation == "4":
            deletetask()
        elif operation == "5":
            check_status()
        elif operation == "6":
            delete_all_tasks()
        elif operation == "7":
            print("Goodbye!!!")
            break
        else:
            print("Invalid input. Please try again!")


if __name__=='__main__':
    menu()