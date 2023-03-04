from time import strftime
import pandas as pd
from tkinter import filedialog
from database.DataBase import DataBase as db

def _export_excel():
    date = str(strftime('%d-%m-%y_%H-%M-%S'))
    name_archivo = f'ListaClientes_{date}.xlsx'
    name, dni, tlf, location, mg, ip, pay, email = [], [], [], [], [], [], [], []
    clients = db()._all_clients()

    for data in clients:
        name.append(data[1])
        dni.append(data[2])
        tlf.append(data[3])
        location.append(data[4])
        mg.append(data[5])
        ip.append(data[6])
        pay.append(data[7])
        email.append(data[8])

    datas = {'Nombre':name, 'DNI':dni, 'TLF':tlf, 'Ubicación':location, 'MG':mg, 'IP':ip, 'Correo':email ,'Estado':pay}
    document_excel = pd.DataFrame(datas,columns=['Nombre', 'DNI', 'TLF', 'Ubicación', 'MG', 'IP', 'Correo' ,'Estado'] )
    document_excel.to_excel((name_archivo), sheet_name='Lista de clientes')