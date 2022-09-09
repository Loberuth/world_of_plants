import sqlite3

class DBUtils:

    @staticmethod
    def executeAndCommit(sqlConnection, query):
        try:
            cursor = sqlConnection.cursor()
            cursor.execute(query)
            sqlConnection.commit()
            cursor.close()
        except sqlite3.Error as sqliteError:
            print(sqliteError)
        except Exception as e:
            print(e)