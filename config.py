import os
from src.utils.sql_db.connect_to_db import ConnectToDb

path = os.path.abspath(__file__)
BASE_PATH = os.path.dirname(path)
MODEL_PATH = os.path.join(BASE_PATH, "data", "model")

endpoint = "https://coringcompany.cognitiveservices.azure.com/"
key = "dcab2ab38d8b4ef6b7d258870992a7be"
API_KEY = "f292c177-b44e-49da-8d27-e3c4ac1f72c1"

# output_type is used in app.py script to identify if the swagger output will be in json format or excel
output_type = "json"

# bot_name is used in save_to_db.py script to insert/update rows in table
bot_name = "TCC"

# Sql database parameters
Flag = "test"

if Flag == "test":
    host = "db"
    user = "root"
    passwd = "root"
    port = "3306",
    database = "documentcount"

if Flag == "local":
    host = "localhost"
    user = "root"
    passwd = "1234"
    database = "documentcount"
else:
    host = "documentbot.mysql.database.azure.com"
    user = "documentbot@documentbot"
    passwd = "Simplifai#2021"
    database = "documentcount"

# database connection
try:
    db_obj = ConnectToDb()
    conn, curr = db_obj.return_connector()
except Exception as e:
    print(e)