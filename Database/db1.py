import sqlite3

#  Create a database in SQLite
con = sqlite3.connect('mydatabase.db')

# Create a table in the database
mycursor = con.cursor()

# mycursor.execute("create table Students(roll_no int primary key,firstname varchar(50),lastname varchar(50)) ")

# mycursor.execute("create table Students2(roll_no int primary key,firstname varchar(50),lastname varchar(50)) ")

# Insert data into the table
# mycursor.execute("insert into Students values(1,'John','Doe')")
# mycursor.execute("insert into Students values(2,'Jane','Roe')")
# mycursor.execute("insert into Students values(3,'John','Smith')")
# con.commit()

# Fetch data from the table
# mycursor.execute("select * from Students")
# # print(mycursor.fetchall())

# mydata = mycursor.fetchall()
# for i in mydata:
#     print(i)
# con.close()

# Create a Questions for the database Employees
# 1. Create a database Employees
# 2. Create a table Employees with the following columns
#    a. emp_id int primary key
#    b. emp_name varchar(50)
#    c. emp_salary int
# 3. Insert data into the table
# 4. Fetch data from the table