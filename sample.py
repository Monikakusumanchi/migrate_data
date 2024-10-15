import pandas as pd
from sqlalchemy import create_engine
import pyodbc

# PostgreSQL connection string
postgres_engine = create_engine("postgresql://admin:admin123@localhost:5432/testdb")

# MS SQL Server ODBC connection string
mssql_connection = pyodbc.connect('DRIVER=/opt/microsoft/msodbcsql17/lib64/libmsodbcsql-17.6.so.1.1;'
                                  'SERVER=localhost;'
                                  'PORT=1433;'
                                  'DATABASE=master;'
                                  'UID=sa;'
                                  'PWD=Monika@1407!')


# Create SQLAlchemy engine for MS SQL Server
mssql_engine = create_engine('mssql+pyodbc://sa:Monika@1407!@localhost:1433/master?driver=ODBC+Driver+17+for+SQL+Server')
# Query to read data from PostgreSQL
query = "SELECT * FROM employees"
df = pd.read_sql(query, postgres_engine)
print("Data from PostgreSQL:")
print(df)
# Write the DataFrame to MS SQL Server
df.to_sql('migrate_table', mssql_engine, if_exists='replace', index=False)
print("Data migrated to MS SQL Server successfully!")

