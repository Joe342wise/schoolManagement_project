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


# def generate_data(tblCourses):
#   """Generates random data for the tblCourses table."""
#   data = []
#   # Assuming you already have data in tblTeachers (generated earlier)
#   teachers = [(row[0]) for row in cursor.execute("SELECT techIdpk FROM tblTeachers")]  # Get teacher IDs

#   for _ in range(50):  # Replace 10 with your desired number of rows
#     course_name = f"Course_{random.randint(1, 1000)}"
#     teacher_id = random.choice(teachers)
#     data.append((course_name, teacher_id))
#   return data


# def insert_data(connection, cursor, tblCourses, data):
#   """Inserts data into the specified table."""
#   try:
#     # Build the insert query dynamically based on column count
#     columns = ", ".join(["?" for _ in range(len(data[0]))])
#     insert_query = f"INSERT INTO {tblCourses} (cosName, techIdpk) VALUES ({columns})"
#     cursor.executemany(insert_query, data)
#     connection.commit()
#     print(f"Successfully inserted {len(data)} rows into {tblCourses}")
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
#     # Assuming tblTeachers data is already inserted, fetch teacher IDs
#     data = generate_data("tblCourses")
#     insert_data(connection, cursor, "tblCourses", data)
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

def generate_data(cursor):
    data = []
    cursor.execute("SELECT techIdpk FROM tblTeachers")
    teachers = [row[0] for row in cursor.fetchall()]
    for _ in range(50):
        course_name = f"Course_{random.randint(1, 1000)}"
        teacher_id = random.choice(teachers)
        data.append((course_name, teacher_id))
    return data

def insert_data(connection, cursor, table_name, data):
    try:
        columns = ", ".join(["%s" for _ in range(len(data[0]))])
        insert_query = f"INSERT INTO {table_name} (cosName, techIdpk) VALUES ({columns})"
        cursor.executemany(insert_query, data)
        connection.commit()
        print(f"Successfully inserted {len(data)} rows into {table_name}")
    except pymysql.Error as err:
        print(f"Error inserting data: {err}")

if __name__ == "__main__":
    host = "localhost"
    user = "root"
    password = "123456789"
    database = "schoolManagementSystem"

    connection, cursor = connect_to_database(host, user, password, database)
    if connection:
        data = generate_data(cursor)
        insert_data(connection, cursor, "tblCourses", data)
        connection.close()
        cursor.close()