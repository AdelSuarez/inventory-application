import customtkinter
from database.DataBase import DataBase as db
import settings.settings as setting


class FunctCreateClient:
    def __init__(self, name_entry, dni_entry, tlf_entry, location, megas_entry, ip_entry, radio_var, message, table, radiobtn_pay, radiobtn_earring):
        self._name_entry = name_entry
        self._dni_entry = dni_entry
        self._tlf_entry = tlf_entry
        self._location = location
        self._megas_entry = megas_entry
        self._ip_entry = ip_entry
        self._radio_var = radio_var
        self._message_client = message
        self.table = table
        self._radiobtn_pay = radiobtn_pay 
        self._radiobtn_earring = radiobtn_earring
        
    
    def _create_client(self):
        self._delete_point(self._ip_entry)
        if len(self._name_entry.get()) != 0 and len(self._dni_entry.get()) != 0 and len(self._tlf_entry.get()) != 0 and len(self._megas_entry.get()) != 0:
            
            if self._validate_empty_int(self._dni_entry.get()) and self._validate_empty_int(self._tlf_entry.get()) and self._validate_empty_int(self._megas_entry.get()) and self._validate_empty_int(self._delete_point(self._ip_entry)):
                if self._location.get() != 'Ubicación':
                    parameters = (self._name_entry.get(), self._dni_entry.get(), self._tlf_entry.get(), self._location.get(), self._megas_entry.get(), self._ip_entry.get(), self._radio_var.get())
                    query = 'INSERT INTO clients VALUES(NULL,?,?,?,?,?,?,?)'
                    db()._connect_db(query, parameters)
                    self.table()
                    self._name_entry.delete(0, customtkinter.END)
                    self._dni_entry.delete(0, customtkinter.END)
                    self._tlf_entry.delete(0, customtkinter.END)
                    self._megas_entry.delete(0, customtkinter.END)
                    self._ip_entry.delete(0, customtkinter.END)
                    self._radiobtn_pay.deselect(0)
                    self._radiobtn_earring.deselect(0)
                    self._location.set("Ubicación")
                    self._message(self._message_client,'Cliente registrado con exito', setting.APPROVED)
                else:
                    self._message(self._message_client,'Introduce la ubicación', setting.WARNING)

            else:
                self._message(self._message_client,'Introduce solo números', setting.WARNING)

        else:
            self._message(self._message_client, 'No dejar Campos vacios', setting.WARNING)

    
    def _validate_empty_int(self, number):
        # Verify that the phone entered is numbers
        value = None
        try:
            if int(number): 
                value = True
        except:
            value = False

        return value
    
    def _delete_point(self, number):
        try:
            ip  = ''
            for i in number.get():
                if i != '.':
                    ip += i
            return int(ip)
        except Exception:
            self._message(self._message_client,'Introduce solo números', setting.WARNING)

    
    def _message(self, message, text, color):
        message.grid(row=9, column=0, columnspan=2, sticky=customtkinter.NSEW)
        message.configure(text=text, fg_color=color, corner_radius=60)
