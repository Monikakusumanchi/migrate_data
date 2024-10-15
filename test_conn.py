# import connectorx as cx

# # Define the connection string
# connection_string = "mssql://SA:Monika@1407!@mssql:1433/testdb"

# # SQL query to execute
# query = "SELECT @@VERSION AS version"

# # Use ConnectorX to read SQL
# try:
#     df = cx.read_sql(query, connection_string)
#     print(df)
# except Exception as e:
#     print(f"An error occurred: {e}")
# import connectorx as cx

# # Define the connection strings for services running in Docker Compose
# mssql_conn = "mssql://SA:Monika@1407!@mssql:1433"
# postgres_conn = "postgres://admin:admin123@postgres:5432/testdb"

# # Define the query to extract data from SQL Server
# query = "SELECT * FROM WideWorldImporters.Warehouse.StockItems"

# # Perform data transfer using ConnectorX
# cx.read_sql( postgres_conn, query )
import connectorx as cx

from sqlalchemy import create_engine

# Define the connection string
connection_string = 'postgresql://admin:admin123@localhost:5432/testdb'
# query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
query = "SELECT * FROM employees"

print(connection_string)
tablenames = cx.read_sql(connection_string, query)
print(tablenames)


# # Replace with your PostgreSQL connection string
db_url = 'mssql://SA:Monika@1407!@localhost:1433/testdb'
query = "SELECT * FROM Inventory"

# Load data into a pandas DataFrame
df = cx.read_sql(db_url, query)

# Print the DataFrame
print(df)
# sql_server_url = "mssql+pyodbc://SA:Monika@1407!@localhost:1433/testdb?driver=ODBC+Driver+17+for+SQL+Server"

# # Create a SQLAlchemy engine
# engine = create_engine(sql_server_url)

# # Insert the DataFrame into SQL Server (replace 'your_table' with the target table name)
# df.to_sql('Emp', con=engine, if_exists='append', index=False)

# print("Data migration to SQL Server is complete!")
# Source PostgreSQL URI
mssql_uri = "postgresql://admin:admin123@localhost:5432/testdb"

# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Send the dataframe to PostgreSQL table (replace 'your_table' with the target table name)
df.to_sql('your_table', con=engine, if_exists='append', index=False)

print("Data has been successfully inserted into the table!")