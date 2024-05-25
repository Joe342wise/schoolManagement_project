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


# def generate_data(tblTeachers):
#   """Generates random data for the tblTeachers table."""
#   data = []
#   subjects = ["Math", "Science", "English", "History", "Social Studies", "Art", "Music", "Physical Education"]
#   for _ in range(100):  # Replace 10 with your desired number of rows
#     first_name = f"Teacher_{random.randint(1, 1000)}"
#     last_name = f"Data_{random.randint(1, 1000)}"
#     subject = random.choice(subjects)
#     email = f"{first_name.lower()}.{last_name.lower()}@{random.randint(1,99)}.com"
#     phone_number = f"0{random.randint(100000000, 999999999)}"
#     data.append((first_name, last_name, subject, email, phone_number))
#   return data


# def insert_data(connection, cursor, tblTeachers, data):
#   """Inserts data into the specified table."""
#   try:
#     # Build the insert query dynamically based on column count
#     columns = ", ".join(["?" for _ in range(len(data[0]))])
#     insert_query = f"INSERT INTO {tblTeachers} (techFirstName, techLastName, techSubjectTought, techEmail, techPhoneNumber) VALUES ({columns})"
#     cursor.executemany(insert_query, data)
#     connection.commit()
#     print(f"Successfully inserted {len(data)} rows into {tblTeachers}")
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
#     data = generate_data("tblTeachers")
#     insert_data(connection, cursor, "tblTeachers", data)
#     connection.close()
#     cursor.close()


import random
import string
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
  """Generates random data for the tblTeachers table."""
  data = []
  subjects = ["Math", "Science", "English", "History", "Social Studies", "Art", "Music", "Physical Education"]
  for _ in range(100):  # Replace 10 with your desired number of rows
    first_name = f"Teacher_{random.randint(1, 1000)}"
    last_name = f"Data_{random.randint(1, 1000)}"
    subject = random.choice(subjects)
    email = f"{first_name.lower()}.{last_name.lower()}@{random.randint(1,99)}.com"
    phone_number = f"0{random.randint(100000000, 999999999)}"
    data.append((first_name, last_name, subject, email, phone_number))
  return data


def insert_data(connection, cursor, tblTeachers, data):
  """Inserts data into the specified table."""
  try:
    # Build the insert query dynamically based on column count
    columns = ", ".join(["%s" for _ in range(len(data[0]))])
    insert_query = f"INSERT INTO {tblTeachers} (techFirstName, techLastName, techSubjectTought, techEmail, techPhoneNumber) VALUES ({columns})"
    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"Successfully inserted {len(data)} rows into {tblTeachers}")
  except pymysql.Error as err:
    print(f"Error inserting data: {err}")


if __name__ == "__main__":
  # Replace with your database connection details (if not using environment variable)
  host = "localhost"
  user = "root"
  password = os.environ.get('MYSQL_ROOT_PASSWORD')
  database = "schoolManagementSystem"

  connection, cursor = connect_to_database(host, user, password, database)
  if connection:
    data = generate_data()  # No need to pass table name here
    insert_data(connection, cursor, "tblTeachers", data)
    connection.close()
    cursor.close()