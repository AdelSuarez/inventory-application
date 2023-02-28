from Manager import Manager
from database.DataBase import DataBase

query_client = '''CREATE TABLE IF NOT EXISTS clients (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        DNI INTEGER NOT NULL,
        TLF INTEGER,
        LOCATION TEXT NOT NULL,
        MG INTEGER NOT NULL,
        IP INTEGER NOT NULL ,
        PAY TEXT
)'''

query_location = ''' CREATE TABLE IF NOT EXISTS location (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                LOCATION TEXT NOT NULL
        )
'''


if __name__ == '__main__':
    print('Run app')
    DataBase()._connect_db(query_client)
    DataBase()._connect_db(query_location)
    app = Manager()
    app.mainloop()
    print('finished app')
