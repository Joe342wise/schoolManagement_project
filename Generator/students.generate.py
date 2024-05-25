# import random
# import datetime
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


# def generate_data(tblStudents):
#   """Generates random data for the tblStudents table."""
#   data = []
#   for _ in range(1000):  # Replace 10 with your desired number of rows
#     first_name = f"Student_{random.randint(1, 1000)}"
#     last_name = f"Data_{random.randint(1, 1000)}"
#     date_of_birth = datetime.date(year=random.randint(2000, 2010), month=random.randint(1, 12), day=random.randint(1, 28))
#     grade_level = random.randint(1, 12)
#     emergency_contact = f"0{random.randint(100000000, 999999999)}"
#     data.append((first_name, last_name, date_of_birth, grade_level, emergency_contact))
#   return data


# def insert_data(connection, cursor, tblStudents, data):
#   """Inserts data into the specified table."""
#   try:
#     # Build the insert query dynamically based on column count
#     columns = ", ".join(["?" for _ in range(len(data[0]))])
#     insert_query = f"INSERT INTO {tblStudents} (stdFirstName, stdLastName, stdDateOfBirth, stdGradeLevel, stdEmergencyContactInfomation) VALUES ({columns})"
#     cursor.executemany(insert_query, data)
#     connection.commit()
#     print(f"Successfully inserted {len(data)} rows into {tblStudents}")
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
#   # password = os.environ.get('MYSQL_ROOT_PASSWORD')
#   password = "123456789"
#   database = "schoolManagementSystem"

#   connection, cursor = connect_to_database(host, user, password, database)
#   if connection:
#     data = generate_data("tblStudents")  # Assuming table name is tblStudents
#     insert_data(connection, cursor, "tblStudents", data)
#     connection.close()
#     cursor.close()


import random
import datetime
import pymysql
import os

def connect_to_database(host, user, password, database):
  """Connects to the database and returns a connection object and cursor."""
  try:
    connection = pymysql.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = connection.cursor()
    return connection, cursor
  except pymysql.Error as err:
    print(f"Error connecting to database: {err}")
    return None, None


def generate_data():
  """Generates random data for the tblStudents table."""
  data = []
  for _ in range(1000):  # Replace 10 with your desired number of rows
    first_name = f"Student_{random.randint(1, 1000)}"
    last_name = f"Data_{random.randint(1, 1000)}"
    date_of_birth = datetime.date(year=random.randint(2000, 2010), month=random.randint(1, 12), day=random.randint(1, 28))
    grade_level = random.randint(1, 12)
    emergency_contact = f"0{random.randint(100000000, 999999999)}"
    data.append((first_name, last_name, date_of_birth, grade_level, emergency_contact))
  return data


def insert_data(connection, cursor, tblStudents, data):
  """Inserts data into the specified table."""
  try:
    # Build the insert query dynamically based on column count
    columns = ", ".join(["%s" for _ in range(len(data[0]))])
    insert_query = f"INSERT INTO {tblStudents} (stdFirstName, stdLastName, stdDateOfBirth, stdGradeLevel, stdEmergencyContactInfomation) VALUES ({columns})"
    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"Successfully inserted {len(data)} rows into {tblStudents}")
  except pymysql.Error as err:
    print(f"Error inserting data: {err}")


if __name__ == "__main__":
  # Replace with your database connection details (if not using environment variable)
  host = "localhost"
  user = "root"
  password = "123456789"
  database = "schoolManagementSystem"

  connection, cursor = connect_to_database(host, user, password, database)
  if connection:
    data = generate_data()  # No need to pass table name here
    insert_data(connection, cursor, "tblStudents", data)
    connection.close()
    cursor.close()