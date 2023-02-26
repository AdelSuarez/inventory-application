import customtkinter
import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from database.DataBase import DataBase as db
import settings.settings as setting
from src.FunctLocation import FunctLocation as fl

class HomeScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(corner_radius=0)
        self.list=[]
        self._configure_win()
        self._controller_frame()
        self._table()

    def _controller_frame(self):
        self._controller = customtkinter.CTkFrame(master=self, corner_radius=0)
        self._controller.grid(row=0, column=0, sticky=customtkinter.NSEW)

        self.tabview = customtkinter.CTkTabview(self._controller)
        self.tabview.grid(row=0, column=0, padx=10, columnspan=2, sticky=customtkinter.NSEW)
        self.tabview.add("Datos de cliente")
        self.tabview.add("Crear cliente")
        self.tabview.add("Configuraciones de Ubicacion")
        self.tabview.tab("Datos de cliente").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Crear cliente").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Configuraciones de Ubicacion").grid_columnconfigure(0, weight=1)
        self._view_client(self.tabview.tab('Datos de cliente'))
        self._create_client(self.tabview.tab('Crear cliente'))
        self._location_settings_view(self.tabview.tab('Configuraciones de Ubicacion'))

        self._controller.columnconfigure(0, weight=1)
        self._controller.columnconfigure(1, weight=1)

    def _view_client(self, wind):
        self._view_client_frame = customtkinter.CTkFrame(wind)
        self._view_client_frame.configure(fg_color='transparent')
        self._view_client_frame.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)

        self._name_title = customtkinter.CTkLabel(self._view_client_frame, text='Nombre:', font=customtkinter.CTkFont( weight="bold"))
        self._name_title.grid(row=0, column=0, padx=(0, 10), pady=10)

        self._name_entry_view = customtkinter.CTkEntry(self._view_client_frame, border_width=0, state='disabled', height=40)
        self._name_entry_view.grid(row=0, column=1, pady=10, sticky=customtkinter.NSEW)

        self._dni_tlf_frame = customtkinter.CTkFrame(self._view_client_frame)
        self._dni_tlf_frame.configure(fg_color='transparent')
        self._dni_tlf_frame.grid(row=1, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._dni_title = customtkinter.CTkLabel(self._dni_tlf_frame, text='DNI:', font=customtkinter.CTkFont( weight="bold"))
        self._dni_title.grid(row=0, column=0, padx=(0,10))

        self._dni_entry_view = customtkinter.CTkEntry(self._dni_tlf_frame, border_width=0, state='disabled', height=40)
        self._dni_entry_view.grid(row=0, column=1, padx=(0,5), sticky=customtkinter.NSEW)

        self._tlf_title = customtkinter.CTkLabel(self._dni_tlf_frame, text='TLF:', font=customtkinter.CTkFont( weight="bold"))
        self._tlf_title.grid(row=0, column=2, padx=(0,10))

        self._tlf_entry_view = customtkinter.CTkEntry(self._dni_tlf_frame, border_width=0, state='disabled', height=40)
        self._tlf_entry_view.grid(row=0, column=3, sticky=customtkinter.NSEW)

        self._location_view = customtkinter.CTkOptionMenu(self._view_client_frame, 
                                                values=["vacio"],
                                                width=200)
        self._location_view.grid(row=4, column=0,pady=10, columnspan=2, sticky=customtkinter.NSEW)
        self._location_view.set("vacio")

        self._mg_ip_frame = customtkinter.CTkFrame(self._view_client_frame)
        self._mg_ip_frame.configure(fg_color='transparent')
        self._mg_ip_frame.grid(row=5, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._mg_title = customtkinter.CTkLabel(self._mg_ip_frame, text='MG:', font=customtkinter.CTkFont( weight="bold"))
        self._mg_title.grid(row=0, column=0, padx=(0,10))

        self._mg_entry_view = customtkinter.CTkEntry(self._mg_ip_frame, border_width=0, state='disabled', height=40)
        self._mg_entry_view.grid(row=0, column=1, padx=(0,5), sticky=customtkinter.NSEW)

        self._ip_title = customtkinter.CTkLabel(self._mg_ip_frame, text='IP:', font=customtkinter.CTkFont( weight="bold"))
        self._ip_title.grid(row=0, column=2, padx=(0,10))

        self._tlf_entry_view = customtkinter.CTkEntry(self._mg_ip_frame, border_width=0, state='disabled', height=40)
        self._tlf_entry_view.grid(row=0, column=3, sticky=customtkinter.NSEW)


        self._btn_frame = customtkinter.CTkFrame(self._view_client_frame)
        self._btn_frame.configure(fg_color='transparent')
        self._btn_frame.grid(row=6, column=0, pady=10, columnspan=2, sticky=customtkinter.NSEW)

        self._btn_delete_location = customtkinter.CTkButton(self._btn_frame, text="Borrar")
        self._btn_delete_location.grid(row=0, column=0, padx=(0,10), sticky=customtkinter.NSEW)
        self._btn_edit_location = customtkinter.CTkButton(self._btn_frame, text="Editar")
        self._btn_edit_location.grid(row=0, column=1, sticky=customtkinter.NSEW)

        self._btn_frame.columnconfigure(0, weight=1)
        self._btn_frame.columnconfigure(1, weight=1)
        self._mg_ip_frame.columnconfigure(1, weight=1)
        self._mg_ip_frame.columnconfigure(3, weight=2)
        self._dni_tlf_frame.columnconfigure(1, weight=1)
        self._dni_tlf_frame.columnconfigure(3, weight=2)
        self._view_client_frame.columnconfigure(1, weight=1)

    def _create_client(self, wind):
        self._logo_img_reset = customtkinter.CTkImage(Image.open(os.path.join("img/", "reset.png")), size=(26, 26))
        self._create_client_frame = customtkinter.CTkFrame(wind)
        self._create_client_frame.configure(fg_color='transparent')
        self._create_client_frame.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)

        self._date = customtkinter.CTkLabel(self._create_client_frame, text="Datos:", font=customtkinter.CTkFont( weight="bold"))
        self._date.grid(row=1, column=0, padx=10, sticky=customtkinter.W)

        self._name_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Nombre del cliente", height=40)
        self._name_entry.grid(row=2, column=0,columnspan=2, sticky=customtkinter.NSEW)

        self._dni_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="DNI", height=40)
        self._dni_entry.grid(row=3, column=0, pady=(10,0), padx=(0, 10), sticky=customtkinter.NSEW)

        self._tlf_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Número telefonico", height=40)
        self._tlf_entry.grid(row=3, column=1, pady=(10,0), sticky=customtkinter.NSEW)
        self.list = db()._locations_optionmenu(self.list)
        
        self._location_frame = customtkinter.CTkFrame(self._create_client_frame, fg_color='transparent')
        self._location_frame.grid(row=4, column=0, columnspan=2,pady=10, sticky=customtkinter.NSEW)
        self._location = customtkinter.CTkOptionMenu(self._location_frame, 
                                                    values=self.list,
                                                    width=200)
        self._location.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._location.set("Ubicación")
        self._location_reset = customtkinter.CTkButton(self._location_frame, text='', image=self._logo_img_reset, width=40, command=self._reset_location)
        self._location_reset.grid(row=0, column=1, padx=(5,0))


        self._megas_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Megas", height=40)
        self._megas_entry.grid(row=5, column=0, padx=(0, 10), sticky=customtkinter.NSEW)

        self._ip_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="IP", height=40)
        self._ip_entry.grid(row=5, column=1, sticky=customtkinter.NSEW)

        self._btn_add_location = customtkinter.CTkButton(self._create_client_frame, text="Crear cliente")
        self._btn_add_location.grid(row=6, column=0, columnspan=2, pady=10, sticky=customtkinter.NSEW)

        self._location_frame.columnconfigure(0, weight=1)
        self._create_client_frame.columnconfigure(0, weight=1)
        self._create_client_frame.columnconfigure(1, weight=1)

    

    def _location_settings_view(self, wind):

        self._location_settings_frame = customtkinter.CTkFrame(wind)
        self._location_settings_frame.configure(fg_color='transparent')
        self._location_settings_frame.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)
        
        self._location_entry = customtkinter.CTkEntry(self._location_settings_frame, placeholder_text='Introduce la ubicación', height=40)
        self._location_entry.grid(row=0, column=0, columnspan=2, pady=10, sticky=customtkinter.NSEW)

        self._btn_location_settings = customtkinter.CTkFrame(self._location_settings_frame)
        self._btn_location_settings.configure(fg_color='transparent')

        self._btn_location_settings.grid(row=1, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._btn_delete_location = customtkinter.CTkButton(self._btn_location_settings, text='Borrar', width=60, command=lambda:fl_parameters._delete_location(), fg_color=setting.WARNING)
        self._btn_delete_location.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._btn_edit_location = customtkinter.CTkButton(self._btn_location_settings, text='Editar', width=60, fg_color=setting.EDIT_COLOR, command=lambda:fl_parameters._edit_location())
        self._btn_edit_location.grid(row=0, column=1, padx=5, sticky=customtkinter.NSEW)
        self._btn_save_location = customtkinter.CTkButton(self._btn_location_settings, text='Guardar', width=60, command=lambda:fl_parameters._save_location())
        self._btn_save_location.grid(row=0, column=2, sticky=customtkinter.NSEW)


        self._table_location = ttk.Treeview(self._location_settings_frame, columns=('location',), padding=[0])
        self._table_location.column('#0')
        self._table_location.heading('#0', text='Ubicación', anchor=tk.CENTER)
        self._table_location.column('#1', width=0, stretch=tk.NO)
        self._table_location.heading("#1",text="",anchor=tk.CENTER)

        self.xscroll = customtkinter.CTkScrollbar(self._location_settings_frame,command=self._table_location.xview)
        self.yscroll = customtkinter.CTkScrollbar(self._location_settings_frame, command=self._table_location.yview)
        self.xscroll.grid(row=2, column=1, sticky='ew')
        self.yscroll.grid(column=1, row=2, sticky='ns')

        self._table_location.configure(yscrollcommand=self.yscroll.set,
                               xscrollcommand=self.xscroll.set)
        self._table_location.grid(row=2, column=0, sticky=customtkinter.NSEW, pady=5)

        self._message = customtkinter.CTkLabel(self._location_settings_frame, text='')
        self._message.grid(row=3, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._btn_location_settings.columnconfigure(0, weight=1)
        self._btn_location_settings.columnconfigure(1, weight=1)
        self._btn_location_settings.columnconfigure(2, weight=1)
        self._location_settings_frame.columnconfigure(0, weight=1)

        fl_parameters = fl(self._location_entry, self._table_location, self._message)
        fl_parameters._get_locations()

# Nombre, ubicacion, IP, MG, Estado
    def _table(self):
        self.table = ttk.Treeview(self, columns=('name', 'location', 'IP', 'MG', 'state'), padding=[0,0,0,0,0])
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.heading("#0",text="",anchor=tk.CENTER)
        self.table.column('name', width=350, anchor=tk.CENTER, stretch=0)
        self.table.heading('name', text='Nombre')
        self.table.column('location',  width=350, anchor=tk.CENTER, stretch=0)
        self.table.heading('location', text='Ubicacion')
        self.table.column('IP', width=110, anchor=tk.CENTER, stretch=0)
        self.table.heading('IP', text='IP')
        self.table.column('MG', width=50, anchor=tk.CENTER, stretch=0)
        self.table.heading('MG', text='MG')
        self.table.column('state', width=70, anchor=tk.CENTER)
        self.table.heading('state', text='Estado')
        self.table.grid(row=0, column=1, sticky=tk.NSEW, pady=10, padx=10)


    def _configure_win(self):
        self.grid(row=1, column=0, sticky=customtkinter.NSEW)
        self.columnconfigure(0, weight=1, minsize=300)
        self.columnconfigure(1, minsize=900)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
    
    def _reset_location(self):
        self.list = db()._locations_optionmenu(self.list)
        self._location.configure(values=self.list)
        print(self.list)
