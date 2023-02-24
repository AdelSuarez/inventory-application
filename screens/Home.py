import customtkinter
import tkinter as tk
from tkinter import ttk

class HomeScreen(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(corner_radius=0)
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

        self._btn_delete = customtkinter.CTkButton(self._btn_frame, text="Borrar")
        self._btn_delete.grid(row=0, column=0, padx=(0,10), sticky=customtkinter.NSEW)
        self._btn_edit = customtkinter.CTkButton(self._btn_frame, text="Editar")
        self._btn_edit.grid(row=0, column=1, sticky=customtkinter.NSEW)

        self._btn_frame.columnconfigure(0, weight=1)
        self._btn_frame.columnconfigure(1, weight=1)
        self._mg_ip_frame.columnconfigure(1, weight=1)
        self._mg_ip_frame.columnconfigure(3, weight=2)
        self._dni_tlf_frame.columnconfigure(1, weight=1)
        self._dni_tlf_frame.columnconfigure(3, weight=2)
        self._view_client_frame.columnconfigure(1, weight=1)

    def _create_client(self, wind):
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

        self._location = customtkinter.CTkOptionMenu(self._create_client_frame, 
                                                values=["vacio"],
                                                width=200)
        self._location.grid(row=4, column=1,pady=10, sticky=customtkinter.W)
        self._location.set("vacio")

        self._btn_add_location = customtkinter.CTkButton(self._create_client_frame, text="Agregar ubicación", command=self._add_location)
        self._btn_add_location.grid(row=4, column=0,pady=10, padx=(0,10), sticky=customtkinter.E)

        self._megas_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Megas", height=40)
        self._megas_entry.grid(row=5, column=0, padx=(0, 10), sticky=customtkinter.NSEW)

        self._ip_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="IP", height=40)
        self._ip_entry.grid(row=5, column=1, sticky=customtkinter.NSEW)

        self._btn_add_location = customtkinter.CTkButton(self._create_client_frame, text="Crear cliente", command=self._add_client)
        self._btn_add_location.grid(row=6, column=0, columnspan=2, pady=10, sticky=customtkinter.NSEW)

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
        self._btn_location_settings.grid(row=1, column=0, sticky=customtkinter.NSEW)

        self._btn_delete = customtkinter.CTkButton(self._btn_location_settings, text='Borrar', width=60, state='disabled')
        self._btn_delete.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._btn_edit = customtkinter.CTkButton(self._btn_location_settings, text='Editar', width=60, state='disabled')
        self._btn_edit.grid(row=0, column=1, padx=5, sticky=customtkinter.NSEW)
        self._btn_save = customtkinter.CTkButton(self._btn_location_settings, text='Guardar', width=60)
        self._btn_save.grid(row=0, column=2, sticky=customtkinter.NSEW)

        self._table_location = ttk.Treeview(self._location_settings_frame, columns=('location',), padding=[0])
        self._table_location.column('#0', width=0, stretch=tk.NO)
        self._table_location.heading("#0",text="",anchor=tk.CENTER)
        self._table_location.column('location', anchor=tk.CENTER)
        self._table_location.heading('location', text='Ubicación')
        self._table_location.grid(row=2, column=0, sticky=customtkinter.NSEW, pady=10)


        self._btn_location_settings.columnconfigure(0, weight=1)
        self._btn_location_settings.columnconfigure(1, weight=1)
        self._btn_location_settings.columnconfigure(2, weight=1)
        self._location_settings_frame.columnconfigure(0, weight=1)

    def _add_client(self):
        print(self.name_entry.get())

    def _add_location(self):
        dialog = customtkinter.CTkInputDialog(text="Ingrese la nueva ubicación:", title="Nueva Ubicación")
        print("Number:", dialog.get_input())


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
