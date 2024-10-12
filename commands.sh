docker compose build
docker compose up -d
curl -L -o wwi.bak 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
sudo docker cp wwi.bak sql1:/var/opt/mssql/backup
sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q 'RESTORE FILELISTONLY FROM DISK = "/var/opt/mssql/backup/wwi.bak"' | tr -s ' ' | cut -d ' ' -f 1-2 
sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd \
   -S localhost -U SA -P Monika@1407! \
   -Q 'RESTORE DATABASE WideWorldImporters FROM DISK = "/var/opt/mssql/backup/wwi.bak" WITH MOVE "WWI_P
rimary" TO "/var/opt/mssql/data/WideWorldImporters.mdf", MOVE "WWI_UserData" TO "/var/opt/mssql/data/Wi
deWorldImporters_userdata.ndf", MOVE "WWI_Log" TO "/var/opt/mssql/data/WideWorldImporters.ldf", MOVE "W
WI_InMemory_Data_1" TO "/var/opt/mssql/data/WideWorldImporters_InMemory_Data_1"'
sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q 'SELECT Name FROM sys.Databases'
sudo docker exec -it mssql /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P 'Monika@1407!' -Q 'SELECT TOP 10 StockItemID, StockItemName FROM WideWorldImporters.Warehouse.StockItems ORDER BY StockItemID'
