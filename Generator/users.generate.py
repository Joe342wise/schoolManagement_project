# import random
# import string

# # Replace with your database library (using pymysql for MySQL in this example)
# import pymysql
# import os

# def connect_to_database(host, user, password, database):
#   """Connects to the database and returns a connection object and cursor."""
#   try:
#     connection = pymysql.connect(
#         host=host, user=user, password=password, database=database
#     )
#     cursor = connection.cursor()
#     return connection, cursor
#   except pymysql.Error as err:
#     print(f"Error connecting to database: {err}")
#     return None, None


# def generate_data(tblUsers):
#   """Generates random data for the tblUsers table."""
#   data = []
#   user_roles = ["admin", "teacher", "student"]
#   num_admins = 5  # Number of admin users to generate
#   num_teachers = 100  # Number of teacher users to generate
#   num_students = 1000 # Number of student users to generate

#   for _ in range(num_admins):  # Replace 10 with your desired number of rows
#     user_name = f"User_{random.randint(1, 1000)}"
#     email = f"{user_name.lower()}@{random.randint(1,99)}.com"
#     # Generate a random password (not secure, for demonstration only)
#     password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
#     role = user_roles[0] # Admin role
#     data.append((user_name, email, password, role))

#   for _ in range(num_teachers):  # Replace 10 with your desired number of rows
#     user_name = f"User_{random.randint(1, 1000)}"
#     email = f"{user_name.lower()}@{random.randint(1,99)}.com"
#     # Generate a random password (not secure, for demonstration only)
#     password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
#     role = user_roles[1] # Teacher role
#     data.append((user_name, email, password, role))

#   for _ in range(num_students):  # Replace 10 with your desired number of rows
#     user_name = f"User_{random.randint(1, 1000)}"
#     email = f"{user_name.lower()}@{random.randint(1,99)}.com"
#     # Generate a random password (not secure, for demonstration only)
#     password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
#     role = user_roles[2] # Student role
#     data.append((user_name, email, password, role))
#   return data


# def insert_data(connection, cursor, tblUsers, data):
#   """Inserts data into the specified table."""
#   try:
#     # Build the insert query dynamically based on column count
#     columns = ", ".join(["?" for _ in range(len(data[0]))])
#     insert_query = f"INSERT INTO {tblUsers} (userName, Email, userPassword, userRole, IsActive) VALUES ({columns})"
#     cursor.executemany(insert_query, data)
#     connection.commit()
#     print(f"Successfully inserted {len(data)} rows into {tblUsers}")
#   except pymysql.Error as err:
#     print(f"Error inserting data: {err}")


# if __name__ == "__main__":
#   # Replace with your database connection details (if not using environment variable)
#   # host = "localhost"
#   # user = "root"
#   # password = "your_password"

#   # Using environment variable for password (more secure)
#   host = "localhost"
#   user = "root"
#   password = os.environ.get('MYSQL_ROOT_PASSWORD')
#   database = "schoolManagementSystem"

#   connection, cursor = connect_to_database(host, user, password, database)
#   if connection:
#     data = generate_data("tblUsers")
#     insert_data(connection, cursor, "tblUsers", data)
#     connection.close()
#     cursor.close()


import random
import string
import pymysql
import os

def connect_to_database(host, user, password, database):
    try:
        connection = pymysql.connect(host=host, user=user, password=password, database=database)
        cursor = connection.cursor()
        return connection, cursor
    except pymysql.Error as err:
        print(f"Error connecting to database: {err}")
        return None, None

def generate_data():
    data = []
    user_roles = ["admin", "teacher", "student"]
    num_admins = 5
    num_teachers = 100
    num_students = 1000
    used_emails = set()

    for _ in range(num_admins):
        user_name = f"User_{random.randint(1, 1000)}"
        email = f"{user_name.lower()}@{random.randint(1,99)}.com"
        while email in used_emails:
            user_name = f"User_{random.randint(1, 1000)}"
            email = f"{user_name.lower()}@{random.randint(1,99)}.com"
        used_emails.add(email)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
        role = user_roles[0]
        data.append((user_name, email, password, role, True))

    for _ in range(num_teachers):
        user_name = f"User_{random.randint(1, 1000)}"
        email = f"{user_name.lower()}@{random.randint(1,99)}.com"
        while email in used_emails:
            user_name = f"User_{random.randint(1, 1000)}"
            email = f"{user_name.lower()}@{random.randint(1,99)}.com"
        used_emails.add(email)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
        role = user_roles[1]
        data.append((user_name, email, password, role, True))

    for _ in range(num_students):
        user_name = f"User_{random.randint(1, 1000)}"
        email = f"{user_name.lower()}@{random.randint(1,99)}.com"
        while email in used_emails:
            user_name = f"User_{random.randint(1, 1000)}"
            email = f"{user_name.lower()}@{random.randint(1,99)}.com"
        used_emails.add(email)
        password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))
        role = user_roles[2]
        data.append((user_name, email, password, role, True))

    return data

def insert_data(connection, cursor, table_name, data):
    try:
        columns = ", ".join(["%s" for _ in range(len(data[0]))])
        insert_query = f"INSERT INTO {table_name} (userName, Email, userPassword, userRole, IsActive) VALUES ({columns})"
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Successfully inserted {len(data)} rows into {table_name}")
    except pymysql.Error as err:
        print(f"Error inserting data: {err}")

if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = os.environ.get('MYSQL_ROOT_PASSWORD')
    database = "schoolManagementSystem"

    connection, cursor = connect_to_database(host, user, password, database)
    if connection:
        data = generate_data()
        insert_data(connection, cursor, "tblUsers", data)
        connection.close()
        cursor.close()