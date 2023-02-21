import sqlite3 as sql

class Database:
    def __init___(self, db = 'DataBase.db'):
        self._db = db

    def _connect_db(self, query, parameters = ()):
        with sql.connect(self.db) as conn:
            self.cur = conn.cursor()
            result = self.cur.execute(query, parameters)
            conn.commit()
        return result

    def fetchall(self):
        return self._connect_db().fetchall()