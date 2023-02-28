import customtkinter
from database.DataBase import DataBase as db
import settings.settings as setting

class FunctView():
    def __init__(self, name_entry, dni_entry, tlf_entry, location, mg_entry, ip_entry, radio_var, date_client, get_clients, message, e_normal, e_clear, e_disabled, radiobtn_pay, radiobtn_earring):
        self._name_entry_view = name_entry
        self._dni_entry_view = dni_entry
        self._tlf_entry_view = tlf_entry
        self._location_view = location
        self._mg_entry_view = mg_entry
        self._ip_entry_view = ip_entry
        self._radio_var_view = radio_var
        self._date_client = date_client
        self._get_clients = get_clients
        self._message_client_view = message
        self._entry_normal = e_normal
        self._entry_clear = e_clear
        self._entry_disabled = e_disabled
        self._radiobutton_pay_view = radiobtn_pay
        self._radiobutton_earring_view = radiobtn_earring
        self._is_edit = False


    def _delete_client(self):
        try:
            query = 'DELETE FROM clients WHERE ID=?'
            parameters=(self._date_client[1], )
            print(parameters)
            db()._connect_db(query, parameters)
            self._message_client_view.configure(text='Cliente borrado', fg_color=setting.APPROVED, corner_radius=60)
            self._get_clients()
            self._entry_normal()
            self._entry_clear()
            self._entry_disabled()
            self._location_radiobtn_deselect()
        except Exception:
            self._message_client_view.configure(text='Seleccione un cliente', fg_color=setting.WARNING, corner_radius=60)

    def _edit_client(self):
        try:
            if self._date_client[0] != '':
                print(self._date_client[0])
                self._entry_normal()
                self._radiobutton_pay_view.configure(state='normal')
                self._radiobutton_earring_view.configure(state='normal')
                self._is_edit = True
                print(self._is_edit)
        except Exception:
            self._message_client_view.configure(text='Seleccione un cliente', fg_color=setting.WARNING, corner_radius=60)

    def _save_edit(self):
        if self._is_edit:
            query = 'UPDATE clients SET NAME=?, DNI=?, TLF=?, LOCATION=?, MG=?, IP=?, PAY=? WHERE ID=?'
            parameters = (self._name_entry_view.get(), self._dni_entry_view.get(), self._tlf_entry_view.get(), self._location_view.get(), self._mg_entry_view.get(), self._ip_entry_view.get(), self._radio_var_view.get(), self._date_client[1])
            db()._connect_db(query, parameters)
            self._message_client_view.configure(text='Cliente actualizado con exito', fg_color=setting.APPROVED, corner_radius=60)
            self._get_clients()
            self._entry_normal()
            self._entry_clear()
            self._entry_disabled()
            self._location_radiobtn_deselect()
            
        else:
            self._message_client_view.configure(text='Seleccione un cliente', fg_color=setting.WARNING, corner_radius=60)

    def _location_radiobtn_deselect(self):
        self._location_view.set("Ubicación")
        self._radiobutton_pay_view.configure(state='disabled')
        self._radiobutton_pay_view.deselect(0)
        self._radiobutton_earring_view.configure(state='disabled')
        self._radiobutton_earring_view.deselect(0)

