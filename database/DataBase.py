import sqlite3 as sql

class DataBase:
    def __init__(self, db = 'DataBase.db'):
        self._db = db

    def _connect_db(self, query, parameters = ()):
        with sql.connect(self._db) as conn:
            self._cur = conn.cursor()
            result = self._cur.execute(query, parameters)
            conn.commit()
        return result

    def _fetchall(self):
        return self._connect_db().fetchall()
    
    def _locations_optionmenu(self, list):
        list = []
        query = 'SELECT * FROM location ORDER BY LOCATION DESC'
        locations = self._connect_db(query).fetchall()
        for i in locations:
            list.append(i[1])
        return list
    
    def _all_clients(self):
        query = 'SELECT * FROM clients ORDER BY LOCATION DESC'
        return self._connect_db(query).fetchall()
        
        
        