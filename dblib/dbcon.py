from databricks import sql


connection = sql.connect(server_hostname= "adb-2380197089486732.12.azuredatabricks.net",
                         http_path= "sql/protocolv1/o/2380197089486732/0916-171417-6r6tbrhq",
                         access_token= "dapiee775ec9dcc06ec2998d1594cd7ce220-3"
                        ) 

cursor = connection.cursor()