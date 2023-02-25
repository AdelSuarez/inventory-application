from database.DataBase import DataBase as db
import customtkinter
import settings.settings as setting


class FunctLocation():
    def __init__(self, location_entry, table_location, message):
        self._location_entry = location_entry
        self._table_location = table_location
        self._mode = 'save'
        self._message = message



    def _save_location(self):
        if len(self._location_entry.get()) == 0:
            self._message.configure(text='Introduce una Ubicación', fg_color=setting.WARNING, corner_radius=60)
            self._mode = 'save'
        else:
            if self._mode == 'save':
                query = 'INSERT INTO location VALUES(NULL,?)'
                parameter = (self._location_entry.get(),) 
                db()._connect_db(query, parameter)
                self._location_entry.delete(0, customtkinter.END)
                self._get_locations()
                self._message.configure(text='Ubicación creada con exito', fg_color=setting.APPROVED, corner_radius=60)
            elif self._mode == 'edit':
                if self._location_entry.get() == self._table_location.item(self._table_location.selection())['text']:
                    return
                else:
                    query = 'UPDATE location SET LOCATION=? WHERE ID=?'
                    parameters = (self._location_entry.get(), self._table_location.item(self._table_location.selection())['values'][0])
                    db()._connect_db(query, parameters)
                    self._get_locations()
                    self._message.configure(text='Ubicación actualizada con exito', fg_color=setting.APPROVED, corner_radius=60)
                    self._mode = 'save'
                    self._location_entry.delete(0, customtkinter.END)


    def _delete_location(self):
        try:
            query = 'DELETE FROM location WHERE ID=?'
            parameters=(self._table_location.item(self._table_location.selection())['values'][0], )
            db()._connect_db(query, parameters)
            self._get_locations()
            self._message.configure(text='Ubicación borrada con exito', fg_color=setting.APPROVED, corner_radius=60)
        except Exception:
            self._message.configure(text='Seleccione una ubicacion', fg_color=setting.WARNING, corner_radius=60)

    def _edit_location(self):
        self._location_entry.delete(0, customtkinter.END)
        location = self._table_location.item(self._table_location.selection())['text']
        if location == '':
            self._message.configure(text='Seleccione una ubicacion', fg_color=setting.WARNING, corner_radius=60)
            print('nada')
            return
        self._message.configure(text='', fg_color='transparent')
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