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
    print("\nSelect an option:")
    print("1. View Full Table")
    print("2. View Completed Tasks")
    print("3. View Pending Tasks")
    print("4. View Ongoing Tasks")
    print("6. Exit")

    try:
        key = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        return

    connection = connectDB()
    cursor = connection.cursor()

    if key == 1:
        query = "SELECT * FROM todos ORDER BY date"
    elif key == 2:
        query = "SELECT * FROM todos WHERE status = 'Completed' ORDER BY date "
    elif key == 3:
        query = "SELECT * FROM todos WHERE status = 'Pending' ORDER BY date "
    elif key == 4:
        query = "SELECT * FROM todos WHERE status = 'Ongoing' ORDER BY date "
 
    elif key == 6:
        print("Exiting show table prompt.")
        connection.close()
        return
    else:
        print("Invalid choice! Please enter a valid number (1-5).")
        connection.close()
        return
    cursor.execute(query)
    tasks = cursor.fetchall()
    if not tasks:
        print("YOUR TO-DO LIST IS EMPTY")
    else:
        print("\nTo-Do List:")
        print("-" * 50)
        for task in tasks:
            print(f"ID: {task[0]} | Task: {task[1]} | Due Date: {task[2]} | Status: {task[3]}")
        print("-" * 50)
    connection.commit()

    connection.close()



def summary_tasks():
    connection = connectDB()
    cursor = connection.cursor()
    print("Summary for your to-do list below:")
    query_sum = 'SELECT status AS summary, COUNT(*) FROM todos GROUP BY status;'
    cursor.execute(query_sum)
    tasks = cursor.fetchall()
    
    for task in tasks:
        print(f"Status: {task[0]} | Total Tasks: {task[1]} ")
        status=task[0]
        query_details = 'SELECT id, task, date FROM todos WHERE status = %s;'
        cursor.execute(query_details, (status,))
        task_details = cursor.fetchall()
        
        if task_details:
                print("  Task Details:")
                for detail in task_details:
                    task_id = detail[0]
                    task_name = detail[1]
                    due_date = detail[2]
                    print(f"- Task ID: {task_id} | Name: {task_name} | Due Date: {due_date}")
                print("\n")
                
        
    connection.commit()
    connection.close()


    
# Tasks: {task[1]}
# GROUP_CONCAT(task SEPARATOR ', ') AS task_details, COUNT(*) AS total_tasks

def create_tasks():
    connection= connectDB()
    cursor=connection.cursor()
    task=input("enter the task  :")
    date= input("enter the due date YYYY-MM-DD  : ")
    print("Recurrence Options: None, Daily, Weekly, Monthly")
    recurrence= input("enter recurrence typee  :")
    # status=input("enter the task status :")
    query = 'INSERT INTO todos (task, date, status, recurrence) VALUES (%s, %s, %s, %s)'
    cursor.execute(query, (task, date, 'Pending', recurrence))
    connection.commit()
    connection.close()
    print(f"Task '{task}' created successfully with recurrence: {recurrence}.")

# create_tasks()

def check_status():
    connection = connectDB()
    cursor = connection.cursor()
    task_id = int(input("Enter the task ID to check status: "))

    query4 = 'SELECT status FROM todos WHERE id = %s'
    cursor.execute(query4, (task_id,))
    result = cursor.fetchone()
    try:
        task_id = int(input("Enter the task ID to check status: "))
    except ValueError:
        print("Invalid input! Please enter a numeric task ID.")
        return

    connection.close()


def update_status():
    connection = connectDB()
    cursor = connection.cursor()
    task_id = int(input("Enter the task ID to update status: "))
    up_status=input("enter the task status (Completed/Pending/Ongoing) :")
    query7 = 'UPDATE todos SET status = %s WHERE id = %s'
    cursor.execute(query7, (up_status, task_id))
    connection.commit()
    connection.close()
    print(f"status for the Task_id = '{task_id}' has been updated successfully. ")




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

def menu():
    while True:
        print("\nSelect an operation to perform:")
        print("1. Create Task")
        print("2. Show Task")
        print("3. update Task details ")
        print("4. Delete single Task")
        print("5. status checker ")
        print("6. update task status ")
        print("7. delete all tasks")
        print("8. to get summary of tasks ")
        print("9. to exit ")
        
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
            update_status()
        elif operation == "7":
            delete_all_tasks()
        elif operation== "8":
            summary_tasks()
        elif operation == "9":
            print("Goodbye!!!") 
            break
        else:
            print("Invalid input. Please try again!")


if __name__=='__main__':
    menu()