# docker compose build
# docker compose up -d
# curl -L -o wwi.bak 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
# sudo docker cp wwi.bak sql1:/var/opt/mssql/backup
# sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q 'RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/wwi.bak"' | tr -s ' ' | cut -d ' ' -f 1-2 
# sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd \
#    -S localhost -U SA -P Monika@1407! \
#    -Q 'RESTORE DATABASE WideWorldImporters FROM DISK = "/var/opt/mssql/backup/wwi.bak" WITH MOVE "WWI_P
# rimary" TO "/var/opt/mssql/data/WideWorldImporters.mdf", MOVE "WWI_UserData" TO "/var/opt/mssql/data/Wi
# deWorldImporters_userdata.ndf", MOVE "WWI_Log" TO "/var/opt/mssql/data/WideWorldImporters.ldf", MOVE "W
# WI_InMemory_Data_1" TO "/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1"'
# sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q 'SELECT Name FROM sys.Databases'
# sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q 'SELECT TOP 10 StockItemID, StockItemName FROM WideWorldImporters.Warehouse.StockItems ORDER BY StockItemID'
# sudo docker exec -u 0 -it sqlserver /bin/bash

# apt-get update
# apt-get install -y mssql-tools unixodbc-dev
# ls /opt/mssql-tools/bin

# docker exec -it mssql "bash"
# /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P Monika@1407!

# CREATE DATABASE TestDB;
# SELECT Name from sys.databases;
# GO
# USE TestDB;
# CREATE TABLE Inventory (id INT, name NVARCHAR(50), quantity INT);
# INSERT INTO Inventory VALUES (1, 'banana', 150); INSERT INTO Inventory VALUES (2, 'orange', 154);
# GO
# SELECT * FROM Inventory WHERE quantity > 152;
# GO
# sudo docker exec -it postgres /bin/bash
# psql -U admin -d testdb
# CREATE TABLE employees (
#     id SERIAL PRIMARY KEY,
#     first_name VARCHAR(50),
#     last_name VARCHAR(50),
#     email VARCHAR(100),
#     department VARCHAR(50),
#     salary NUMERIC(10, 2)
# );
# INSERT INTO employees (first_name, last_name, email, department, salary)
# VALUES ('John', 'Doe', 'john.doe@example.com', 'Engineering', 75000.00);

# INSERT INTO employees (first_name, last_name, email, department, salary)
# VALUES ('Jane', 'Smith', 'jane.smith@example.com', 'HR', 65000.00);

# INSERT INTO employees (first_name, last_name, email, department, salary)
# VALUES ('Alice', 'Johnson', 'alice.johnson@example.com', 'Marketing', 70000.00);

# INSERT INTO employees (first_name, last_name, email, department, salary)
# VALUES 
#     ('Bob', 'Williams', 'bob.williams@example.com', 'Engineering', 72000.00),
#     ('Eve', 'Davis', 'eve.davis@example.com', 'Finance', 68000.00),
#     ('Charlie', 'Brown', 'charlie.brown@example.com', 'IT', 80000.00);

# sudo docker exec -it postgres psql -U admin -d testdb -c "SELECT * FROM employees;"
# sudo docker exec -it postgres pg_dump -U admin -d testdb -f /tmp/testdb_dump.sql
# sudo docker cp postgres:/tmp/testdb_dump.sql ./postgres_data/testdb_dump.sql
# sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q "SELECT @@VERSION"
pip install pyodbc
sudo apt-get update
sudo apt-get install -y unixodbc-dev
# Add the Microsoft package repository
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update

# Install the ODBC Driver for SQL Server
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17
