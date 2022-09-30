from databricks import sql
from configparser import ConfigParser
config = ConfigParser()
config.read(r'./config/keys_config.cfg')


connection = sql.connect(server_hostname= config.get("databricks", "server_hostname"),
                         http_path= config.get("databricks", "http_path"),
                         access_token=config.get("databricks", "access_token")
                        ) 

cursor = connection.cursor()

#build query
def query(tablename, limit):
    cursor.execute("USE nycdata_db;")
    cursor.execute(f"SELECT * FROM {tablename} LIMIT {limit}")
    result = cursor.fetchall()
    for row in result:
        print(row)
        
#sort query


