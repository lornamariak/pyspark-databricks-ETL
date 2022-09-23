#Establish db connection from sqlite3 import connect
from databricks import sql
from configparser import ConfigParser
config = ConfigParser()
config.read(r'./config/keys_config.cfg')


connection = sql.connect(server_hostname= config.get("databricks", "server_hostname"),
                         http_path= config.get("databricks", "http_path"),
                         access_token=config.get("databricks", "access_token")
                        ) 

cursor = connection.cursor()
#test connection
cursor.execute("USE nycdata_db;")
cursor.execute("SELECT * FROM offence LIMIT 2")
result = cursor.fetchall()
for row in result:
    print(row)