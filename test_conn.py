
# import connectorx as cx

# from sqlalchemy import create_engine

# connection_string = 'postgresql://admin:admin123@localhost:5432/testdb'
# # query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
# query = "SELECT * FROM employees"

# print(connection_string)
# tablenames = cx.read_sql(connection_string, query)
# print(tablenames)


# db_url = 'mssql://SA:Monika@1407!@localhost:1433/testdb'
# query = "SELECT * FROM Inventory"

# df = cx.read_sql(db_url, query)

# print(df)

# mssql_uri = "postgresql://admin:admin123@localhost:5432/testdb"

# engine = create_engine(connection_string)

# df.to_sql('your_table', con=engine, if_exists='append', index=False)

# print("Data has been successfully inserted into the table!")
# ==================================
import pyodbc
from sqlalchemy import create_engine
import pandas as pd

# Connection string parameters
server = 'localhost'         # e.g., 'localhost'
port = '5432'                # PostgreSQL default port
database = 'testdb'   # e.g., 'testdb'
username = 'admin'   # PostgreSQL username
password = 'admin123'   # PostgreSQL password

# Create an SQLAlchemy engine for PostgreSQL
engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{server}:{port}/{database}')

# Define your query
query = "SELECT * FROM your_table;"

# Use pandas to read from PostgreSQL using SQLAlchemy
df = pd.read_sql(query, engine)
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
}
df = pd.DataFrame(data)
df['id'] = df['id'].astype(int)
df['name'] = df['name'].astype(str)
df['age'] = df['age'].astype(int)
connection_string = (
    "DRIVER={PostgreSQL ANSI};"
    f"Server={server};"
    f"Port={port};"
    f"Database={database};"
    f"Uid={username};"
    f"Pwd={password};"
    f"sslmode=prefer;"
)
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Create table if it doesn't exist
create_table_sql = """
CREATE TABLE IF NOT EXISTS my_table (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);
"""
cursor.execute(create_table_sql)
conn.commit()  # Commit the transaction

# data_to_insert = [tuple(row) for row in df.itertuples(index=False)]

# # Insert data using executemany
# sql = "INSERT INTO my_table (id, name, age) VALUES (?, ?, ?)"
# cursor.executemany(sql, data_to_insert)

# # Commit the insert transactions
# conn.commit()

# # Close the cursor and connection
# cursor.close()
# conn.close()
test_insert_sql = "INSERT INTO my_table (id, name, age) VALUES (4, 'Test', 40)"
cursor.execute(test_insert_sql)
conn.commit()