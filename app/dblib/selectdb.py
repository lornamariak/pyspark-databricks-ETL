from databricks import sql
from configparser import ConfigParser
config = ConfigParser()
config.read(r'./config/keys_config.cfg')


connection = sql.connect(server_hostname= config.get("databricks", "server_hostname"),
                         http_path= config.get("databricks", "http_path"),
                         access_token=config.get("databricks", "access_token")
                        ) 

cursor = connection.cursor()

#select a database
def selectdb(dbname):
    cursor.execute(f"USE {dbname};")
    print(cursor.execute("SELECT CURRENT_DATABASE();"))

selectdb("nycdata_db")


