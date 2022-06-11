import os
sql_host = os.getenv('_SQL_HOST')
sql_user = os.getenv('_SQL_USER')
sql_password = os.getenv('_SQL_PASSWORD')
sql_database = os.getenv('_SQL_DATABASE')
print(sql_host,sql_user,sql_password,sql_database)