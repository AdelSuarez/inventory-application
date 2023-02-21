import sqlite3 as sql

class DataBase:
    def __init__(self, db = 'DataBase.db'):
        self._db = db

    def _connect_db(self, query, parameters = ()):
        with sql.connect(self._db) as conn:
            self._cur = conn.cursor()
            result = self.cur.execute(query, parameters)
            conn.commit()
        return result

    def _fetchall(self):
        return self._connect_db().fetchall()
        