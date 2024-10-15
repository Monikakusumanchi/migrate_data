import pandas as pd
import pyodbc
import psycopg2

# Step 1: Connect to PostgreSQL
postgres_conn = psycopg2.connect(
    database="testdb",
    user="admin",
    password="admin123",
    host="localhost",
    port="5432"
)

# Step 2: Connect to MS SQL Server using pyodbc
mssql_connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                  'SERVER=localhost;'
                                  'PORT=1433;'
                                  'DATABASE=master;'
                                  'UID=sa;'
                                  'PWD=Monika@1407!')

# Step 3: Load data from PostgreSQL
postgres_query = "SELECT * FROM employees"  # Modify with your table name
df = pd.read_sql_query(postgres_query, postgres_conn)

# Step 4: Create table in MS SQL Server (optional, if you want to create it manually)
# Use pyodbc cursor to create the table (you can skip this if the table already exists)

cursor = mssql_connection.cursor()

# Example to create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS migrate_table (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    salary FLOAT
)
""")
mssql_connection.commit()

# Step 5: Write data to MS SQL Server using pyodbc and pandas
# Insert data into MS SQL Server from the DataFrame

for index, row in df.iterrows():
    cursor.execute("INSERT INTO migrate_table (id, name, age, salary) VALUES (?, ?, ?, ?)", 
                   row['id'], row['name'], row['age'], row['salary'])
    
mssql_connection.commit()
cursor.close()

print("Data migration from PostgreSQL to MS SQL Server completed.")

# Close connections
postgres_conn.close()
mssql_connection.close()
