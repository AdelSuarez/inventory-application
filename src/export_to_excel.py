from time import strftime
import pandas as pd
from database.DataBase import DataBase as db

def _export_excel():
    i = -1
    name, dni, tlf, location, mg, ip, pay = [], [], [], [], [], [], []
    clients = db()._all_clients()
    for data in clients:
        i += 1
        name.append(clients[i][1])
        dni.append(clients[i][2])
        tlf.append(clients[i][3])
        location.append(clients[i][4])
        mg.append(clients[i][5])
        ip.append(clients[i][6])
        pay.append(clients[i][7])

    date = str(strftime('%d-%m-%y_%H-%M-%S'))
    datas = {'Nombre':name, 'DNI':dni, 'TLF':tlf, 'Ubicación':location, 'MG':mg, 'IP':ip, 'Estado':pay}
    document_excel = pd.DataFrame(datas,columns=['Nombre', 'DNI', 'TLF', 'Ubicación', 'MG', 'IP', 'Estado'] )
    document_excel.to_excel((f'ListaClientes {date}.xlsx'))