import sqlite3
from utils.DBUtils import DBUtils

DATABASE_NAME = "PyFlora.db"

class Services:
    def __init__(self):
        self.sqlConnection = sqlite3.connect(DATABASE_NAME)

    def deleteFromDB(self, id, tablename):
        query = f'''
            DELETE FROM {tablename} WHERE id = {id}
        '''
        DBUtils.executeAndCommit(self.sqlConnection, query)

    def updateAPotInDB(self, id, tablename, plant, status, humidity, brightness):
        query = f'''
               UPDATE {tablename} SET plant="{plant}", status="{status}", humidity="{humidity}", brightness="{brightness}" WHERE id ={id}"
           '''
        DBUtils.executeAndCommit(self.sqlConnection, query)