import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="12345", host="127.0.0.1", port="5432")
print("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE patients
      (Customer_Name VARCHAR(255) PRIMARY KEY NOT NULL,
      Customer_Id  VARCHAR(18) NOT NULL,
      Open_Date  Date  NOT NULL,
      Last_Consulted_Date  Date,
      Vaccination_Id CHAR(5),
      Dr_Name CHAR(255),
      State CHAR(5),
      Country VARCHAR(5),
      post INT,
      DOB Date,
      Is_Active CHAR(1));''')
print("Table created successfully")

conn.commit()
conn.close()
