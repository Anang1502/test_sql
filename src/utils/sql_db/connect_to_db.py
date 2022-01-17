import mysql.connector
import config as cf


class ConnectToDb:

    def __init__(self):
        self.conn = mysql.connector.connect(host=cf.host, user=cf.user, passwd=cf.passwd, database=cf.database)
        self.curr = self.conn.cursor()

    def return_connector(self):
        return self.conn, self.curr
