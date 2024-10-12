import connectorx as cx

# SQL Server connection string
sqlserver_conn = "mssql://sa:YourPassword123!@sqlserver:1433/AdventureWorks?driver=ODBC+Driver+17+for+SQL+Server"

# PostgreSQL connection string
postgres_conn = "postgresql://admin:admin123@postgres:5432/testdb"

# SQL query to extract data from AdventureWorks (replace 'your_table_name' with actual table name)
query = "SELECT * FROM your_table_name"

# Migrate data from SQL Server to PostgreSQL
cx.write_sql_table(postgres_conn, sqlserver_conn, query)
print("Data migrated successfully!")
