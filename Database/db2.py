# Import 
import sqlite3

# Connect DB : 
conn = sqlite3.connect('royal.db')
# print(conn)

# Approve : (Cursor)
mycursor = conn.cursor()
# print(mycursor)

# How To Create a Table.
# mycursor.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS student (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(100),
#         age INT,
#         grade VARCHAR(10)
#     )
#     '''
# )
# conn.commit()

# How To Insert Data in a Table.
# mycursor.execute(
#     '''
#         INSERT INTO student (name, age, grade) VALUES
#         ('John Doe', 15, '10th'),
#         ('Jane Smith', 16, '11th'),
#         ('Michael Johnson', 14, '9th'),
#         ('Emily Davis', 17, '12th'),
#         ('Daniel Brown', 15, '10th'),
#         ('Sophia Wilson', 16, '11th'),
#         ('David Martinez', 14, '9th'),
#         ('Olivia Taylor', 17, '12th'),
#         ('James Anderson', 15, '10th'),
#         ('Emma Thomas', 16, '11th')
#     '''
# )
# conn.commit()


# How To Read Data in a Table.
mycursor.execute('select * from student')
mydata = mycursor.fetchall()
for i in mydata : 
    print(i)

# How To Update Data in a Table. 
# mycursor.execute('update student set name="Himesh" where name="John Doe"')
# conn.commit()

# How To Delete Data in a Table.
# mycursor.execute('delete from student where name like "J%"')
# conn.commit()

# Drop : 
# mycursor.execute('drop table student')
# conn.commit()


# DB Close : 
conn.close()


# 
'''
Basic Questions:
How do you create an employee table with columns id, name, age, department, salary, and joining_date?
Write an SQL query to insert five records into the employee table.
How do you retrieve all data from the employee table?
How do you select only name and salary from the employee table?
How do you find the total number of employees in the employee table?
Filtering and Sorting:
Write a query to find employees who work in the "HR" department.
How do you find employees with a salary greater than 50,000?
How do you sort employees by joining_date in descending order?
Write a query to fetch employees whose names start with "A."
How do you find employees between the age of 25 and 35?
Aggregation and Grouping:
How do you calculate the average salary of employees?
Write a query to count the number of employees in each department.
Find the highest and lowest salaries in the employee table.
How do you get the total salary paid to employees in each department?
How do you find the department with the maximum number of employees?
Updating and Deleting Data:
Write an SQL query to update the salary of an employee named "John Doe" to 60,000.
How do you delete employees from the "Sales" department?
Write a query to remove employees who joined before the year 2015.
How do you change the department of an employee with id = 5 to "Finance"?
Write a query to drop the employee table completely.
'''

