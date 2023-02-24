from Manager import Manager
from database.DataBase import DataBase

query = '''CREATE TABLE IF NOT EXISTS clients (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        DNI INTEGER NOT NULL UNIQUE,
        TLF INTEGER,
        LOCATION TEXT NOT NULL,
        MG INTEGER NOT NULL,
        IP INTEGER NOT NULL UNIQUE,
        PAY TEXT
)'''


if __name__ == '__main__':
    print('Run app')
    DataBase()._connect_db(query)
    app = Manager()
    app.mainloop()