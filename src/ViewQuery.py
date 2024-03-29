import customtkinter
from database.DataBase import DataBase as db
import settings.settings as setting
from src.checkers  import validate_empty_int , delete_point


class ViewQuery:
    def __init__(self, name_entry, dni_entry, tlf_entry, location, mg_entry, ip_entry, email_entry, radio_var, data_client, get_clients, message, e_normal, e_clear, e_disabled, radiobtn_pay, radiobtn_earring, counter_client):
        self._name_entry_view = name_entry
        self._dni_entry_view = dni_entry
        self._tlf_entry_view = tlf_entry
        self._location_view = location
        self._mg_entry_view = mg_entry
        self._ip_entry_view = ip_entry
        self._email_entry = email_entry
        self._radio_var_view = radio_var
        self._data_client = data_client
        self._get_clients = get_clients
        self._message_client_view = message
        self._entry_normal = e_normal
        self._entry_clear = e_clear
        self._entry_disabled = e_disabled
        self._radiobutton_pay_view = radiobtn_pay
        self._radiobutton_earring_view = radiobtn_earring
        self._is_edit = False
        self._counter_client = counter_client


    def _delete_client(self):
        try:
            query = 'DELETE FROM clients WHERE ID=?'
            parameters=(self._data_client[1], )
            db()._connect_db(query, parameters)
            self._get_clients()
            self._entry_normal()
            self._entry_clear()
            self._entry_disabled()
            self._location_radiobtn_deselect()
            self._counter_client()
            self._message(self._message_client_view, 'Cliente borrado con exito', setting.APPROVED)
        except Exception:
            self._message(self._message_client_view, 'Seleccione un cliente', setting.WARNING)

    def _edit_client(self):
        try:
            self._message_client_view.grid_forget()
            if self._data_client[0] != '':
                self._entry_normal()
                self._radiobutton_pay_view.configure(state='normal')
                self._radiobutton_earring_view.configure(state='normal')
                self._is_edit = True
        except Exception:
            self._message(self._message_client_view, 'Seleccione un cliente', setting.WARNING)

    def _save_edit(self):
        if self._is_edit:
            delete_point(self._ip_entry_view, self._message(self._message_client_view,'Introduce solo números', setting.WARNING))
            if len(self._name_entry_view.get()) != 0 and len(self._dni_entry_view.get()) != 0 and len(self._tlf_entry_view.get()) != 0 and len(self._mg_entry_view.get()) != 0:

                if validate_empty_int(self._dni_entry_view.get()) and validate_empty_int(self._tlf_entry_view.get()) and validate_empty_int(self._mg_entry_view.get()) and validate_empty_int(delete_point(self._ip_entry_view, self._message(self._message_client_view,'Introduce solo números', setting.WARNING))):

                    if self._location_view.get() != 'Ubicación':
                        self._is_edit = False
                        query = 'UPDATE clients SET NAME=?, DNI=?, TLF=?, LOCATION=?, MG=?, IP=?, PAY=?, EMAIL=? WHERE ID=?'
                        parameters = (self._name_entry_view.get(), self._dni_entry_view.get(), self._tlf_entry_view.get(), self._location_view.get(), self._mg_entry_view.get(), self._ip_entry_view.get(), self._radio_var_view.get(), self._email_entry.get(), self._data_client[1])
                        db()._connect_db(query, parameters)
                        self._get_clients()
                        self._entry_normal()
                        self._entry_clear()
                        self._entry_disabled()
                        self._location_radiobtn_deselect()
                        self._counter_client()

                        self._message(self._message_client_view,'Cliente actualizado con exito', setting.APPROVED)
                    else:
                        self._message(self._message_client_view,'Introduce la ubicación', setting.WARNING)

                else:
                    self._message(self._message_client_view, 'Introduce solo números', setting.WARNING)

            else:
                self._message(self._message_client_view, 'No dejar Campos vacios', setting.WARNING)

        else:
            if self._data_client:
                self._message(self._message_client_view, 'Edite el cliente', setting.WARNING)   
            else:
                self._message(self._message_client_view, 'Seleccione un cliente', setting.WARNING)



    def _location_radiobtn_deselect(self):
        self._location_view.set("Ubicación")
        self._radiobutton_pay_view.configure(state='disabled')
        self._radiobutton_pay_view.deselect(0)
        self._radiobutton_earring_view.configure(state='disabled')
        self._radiobutton_earring_view.deselect(0)
    
        
    def _message(self, message, text, color):
        message.grid(row=10, column=0, columnspan=2, sticky=customtkinter.NSEW)
        message.configure(text=text, fg_color=color, corner_radius=60)

