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


# def generate_data(tblEnrollments):
#   """Generates random data for the tblEnrollments table."""
#   data = []
#   # Assuming you already have data in tblStudents and tblCourses (generated earlier)
#   students = [(row[0]) for row in cursor.execute("SELECT stdIdpk FROM tblStudents")]
#   courses = [(row[0]) for row in cursor.execute("SELECT cosIdpk FROM tblCourses")]

#   for _ in range(1000):  # Replace 10 with your desired number of rows
#     student_id = random.choice(students)
#     course_id = random.choice(courses)
#     data.append((student_id, course_id))
#   return data


# def insert_data(connection, cursor, tblEnrollments, data):
#   """Inserts data into the specified table."""
#   try:
#     # Build the insert query dynamically based on column count
#     columns = ", ".join(["?" for _ in range(len(data[0]))])
#     insert_query = f"INSERT INTO {tblEnrollments} (stdIdpk, cosIdpk) VALUES ({columns})"
#     cursor.executemany(insert_query, data)
#     connection.commit()
#     print(f"Successfully inserted {len(data)} rows into {tblEnrollments}")
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
#     # Assuming tblStudents and tblCourses data are already inserted, fetch IDs
#     data = generate_data("tblEnrollments")
#     insert_data(connection, cursor, "tblEnrollments", data)
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
    cursor.execute("SELECT stdIdpk FROM tblStudents")
    students = [row[0] for row in cursor.fetchall()]
    cursor.execute("SELECT cosIdpk FROM tblCourses")
    courses = [row[0] for row in cursor.fetchall()]
    for _ in range(1000):
        student_id = random.choice(students)
        course_id = random.choice(courses)
        data.append((student_id, course_id))
    return data

def insert_data(connection, cursor, table_name, data):
    try:
        columns = ", ".join(["%s" for _ in range(len(data[0]))])
        insert_query = f"INSERT INTO {table_name} (stdIdpk, cosIdpk) VALUES ({columns})"
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
        insert_data(connection, cursor, "tblEnrollments", data)
        connection.close()
        cursor.close()
        