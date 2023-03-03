import customtkinter
from database.DataBase import DataBase as db
import customtkinter
import settings.settings as setting


class LocationQuery:
    def __init__(self, location_entry, table_location, message):
        self._location_entry = location_entry
        self._table_location = table_location
        self._mode = 'save'
        self._message_location = message



    def _save_location(self):
        if len(self._location_entry.get()) == 0:
            self._message(self._message_location, 'Introduce una Ubicación', setting.WARNING)
            self._mode = 'save'
        else:
            if self._mode == 'save':
                query = 'INSERT INTO location VALUES(NULL,?)'
                parameter = (self._location_entry.get(),) 
                db()._connect_db(query, parameter)
                self._location_entry.delete(0, customtkinter.END)
                self._get_locations()
                self._message(self._message_location, 'Guardado con exito', setting.APPROVED)

            elif self._mode == 'edit':
                if self._location_entry.get() == self._table_location.item(self._table_location.selection())['text']:
                    return
                else:
                    query = 'UPDATE location SET LOCATION=? WHERE ID=?'
                    parameters = (self._location_entry.get(), self._table_location.item(self._table_location.selection())['values'][0])
                    db()._connect_db(query, parameters)
                    self._get_locations()
                    self._mode = 'save'
                    self._location_entry.delete(0, customtkinter.END)
                    self._message(self._message_location, 'Actualizado con exito', setting.APPROVED)



    def _delete_location(self):
        try:
            query = 'DELETE FROM location WHERE ID=?'
            parameters=(self._table_location.item(self._table_location.selection())['values'][0], )
            db()._connect_db(query, parameters)
            self._get_locations()
            self._location_entry.delete(0, customtkinter.END)
            self._message(self._message_location, 'Ubicación borrada con exito', setting.APPROVED)

        except Exception as e:
            self._message(self._message_location, 'Seleccione una ubicación', setting.WARNING)

    def _edit_location(self):
        self._location_entry.delete(0, customtkinter.END)
        location = self._table_location.item(self._table_location.selection())['text']
        if location == '':
            self._message(self._message_location, 'Seleccione una ubicación', setting.WARNING)
            return
        self._message_location.grid_forget()
        self._location_entry.insert(0, location)
        self._mode = 'edit'

    def _get_locations(self):
        locations_table = self._table_location.get_children()
        for element in locations_table:
            self._table_location.delete(element)

        query = 'SELECT * FROM location ORDER BY LOCATION DESC'
        locations = db()._connect_db(query)
        for location in locations:
            self._table_location.insert('', 0, text=location[1] , values=[location[0]])


    def _message(self, message, text, color):
        message.grid(row=3, column=0, columnspan=2, sticky=customtkinter.NSEW)
        message.configure(text=text, fg_color=color, corner_radius=60)

    