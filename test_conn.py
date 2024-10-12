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
import connectorx as cx

# Define the connection strings for services running in Docker Compose
mssql_conn = "mssql://SA:Monika@1407!@mssql:1433"
postgres_conn = "postgres://admin:admin123@postgres:5432/testdb"

# Define the query to extract data from SQL Server
query = "SELECT * FROM WideWorldImporters.Warehouse.StockItems"

# Perform data transfer using ConnectorX
cx.read_sql( postgres_conn, query )