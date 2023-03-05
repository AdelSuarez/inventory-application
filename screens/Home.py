import customtkinter
import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from database.DataBase import DataBase as db
import settings.settings as setting
from src.LocationQuery import LocationQuery as lq
from src.CreateClientQuery import CreateClientQuery as qc
from src.ViewQuery import ViewQuery as vq
from src.export_to_excel import _export_excel
from components.NavBar import Navbar
from components.NotificationBar import NotificationBar

class HomeScreen(customtkinter.CTkFrame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.data_client = []
        self.list=[]
        self._icon_reset = customtkinter.CTkImage(Image.open(os.path.join("img/", "reset2.png")), size=(28, 28))
        self._configure_self()
        self.navbar = Navbar(self, self.manager)
        self._init_widgets()
        self.notification_var= NotificationBar(self)
        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Oswald', 12)) # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Oswald', 12,'bold')) # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders


    def _init_widgets(self):
        self._init_frame = customtkinter.CTkFrame(master=self, corner_radius=0)
        self._init_frame.grid(row=1, column=0, sticky=customtkinter.NSEW)
        self._query_widgets(self._init_frame)
        self._table(self._init_frame)

        # settings
        self._init_frame.rowconfigure(0, weight=1)
        self._init_frame.columnconfigure(0, weight=1, minsize=300)
        self._init_frame.columnconfigure(1,weight=1, minsize=900)

    def _query_widgets(self, master):
        self._controller = customtkinter.CTkFrame(master, corner_radius=0)
        self._controller.grid(row=0, column=0, sticky=customtkinter.NSEW)

        self._tabview = customtkinter.CTkTabview(self._controller)
        self._tabview.grid(row=0, column=0, padx=10, columnspan=2, sticky=customtkinter.NSEW)
        self._tabview.add("Datos de cliente")
        self._tabview.add("Crear cliente")
        self._tabview.add("Configuraciones de Ubicación")
        self._tabview.tab("Datos de cliente").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self._tabview.tab("Crear cliente").grid_columnconfigure(0, weight=1)
        self._tabview.tab("Configuraciones de Ubicación").grid_columnconfigure(0, weight=1)
        self._view_client(self._tabview.tab('Datos de cliente'))
        self._create_client(self._tabview.tab('Crear cliente'))
        self._location_settings_view(self._tabview.tab('Configuraciones de Ubicación'))

        # States Frame
        self._statistics_frame(self._controller)
        self._btn_frame_main(self._controller)

        # Settings Frame
        self._controller.columnconfigure(0, weight=1)
        self._controller.columnconfigure(1, weight=1)
        self._controller.rowconfigure(0, weight=1)
        self._counter()

    def _btn_frame_main(self, main):
        self._btn_main = customtkinter.CTkFrame(main, fg_color='transparent')
        self._btn_main.grid(row=2, column=0, padx=10, pady=(0,10), columnspan=2, sticky=customtkinter.NSEW)

        self._btn_export_excel = customtkinter.CTkButton(self._btn_main, text='Exportar a Excel', command=lambda:_export_excel())
        self._btn_export_excel.grid(row=0, column=0, sticky=customtkinter.E)
        
        self._btn_main.columnconfigure(0, weight=1)

    def _statistics_frame(self, main):
        self._state_frame = customtkinter.CTkFrame(main)
        self._state_frame.grid(row=1, column=0, columnspan=2,pady=10,padx=10 , sticky=customtkinter.NSEW)
    
        self._state_title = customtkinter.CTkLabel(self._state_frame, text='Estadisticas', fg_color=setting.BACKGROUND, corner_radius=5)
        self._state_title.grid(row=0, column=0, columnspan=2, pady=5, padx=5 ,sticky=customtkinter.NSEW)

        self._label_state_frame = customtkinter.CTkFrame(self._state_frame, fg_color='transparent')
        self._label_state_frame.grid(row=1, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._counter_client_title = customtkinter.CTkLabel(self._label_state_frame, text='Clientes:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_client_title.grid(row=0, column=0, pady=(5,0), padx=(10, 0), sticky= customtkinter.W)
        self._counter_client_state = customtkinter.CTkLabel(self._label_state_frame, text='0' ,font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_client_state.grid(row=0, column=1, pady=(5,0), padx=(0, 10), sticky= customtkinter.E )

        self._counter_mg_title = customtkinter.CTkLabel(self._label_state_frame, text='Megas vendidos:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_mg_title.grid(row=1, column=0, pady=(5,0), padx=(10, 0), sticky= customtkinter.W)

        self._counter_mg_state = customtkinter.CTkLabel(self._label_state_frame, text='0', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_mg_state.grid(row=1, column=1, pady=(5,0), padx=(0, 10), sticky= customtkinter.E )
        
        
        self._mg_state_frame = customtkinter.CTkFrame(self._state_frame, fg_color='transparent')
        self._mg_state_frame.grid(row=2, column=0, columnspan=2, sticky=customtkinter.NSEW)
        self._counter_mg_title_pay = customtkinter.CTkLabel(self._mg_state_frame, text='Megas Pagos:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_mg_title_pay.grid(row=0, column=0, pady=5, padx=(10, 0), sticky= customtkinter.W)

        self._counter_mg_state_pay = customtkinter.CTkLabel(self._mg_state_frame, text='0', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_mg_state_pay.grid(row=0, column=1, pady=5, padx=(0, 10), sticky= customtkinter.E )
        
        self._counter_mg_title_earring = customtkinter.CTkLabel(self._mg_state_frame, text='Megas Pendientes:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_mg_title_earring.grid(row=0, column=2, pady=5, padx=(10, 0), sticky= customtkinter.W)

        self._counter_mg_state_earring = customtkinter.CTkLabel(self._mg_state_frame, text='0', font=customtkinter.CTkFont( weight=setting.FONT))
        self._counter_mg_state_earring.grid(row=0, column=3, pady=5, padx=(0, 10), sticky= customtkinter.E )

        self._state_frame.columnconfigure(0, weight=1)
        self._label_state_frame.columnconfigure(0, weight=1)
        self._label_state_frame.columnconfigure(1, weight=1)
        self._mg_state_frame.columnconfigure(0, weight=1)
        self._mg_state_frame.columnconfigure(3, weight=1)

    def _view_client(self, wind):
        self._view_client_frame = customtkinter.CTkFrame(wind)
        self._view_client_frame.configure(fg_color='transparent')
        self._view_client_frame.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)

        self._name_view_frame = customtkinter.CTkFrame(self._view_client_frame, fg_color='transparent')
        self._name_view_frame.grid(row=0, column=0, columnspan=2, sticky=customtkinter.NSEW, pady=10)
        self._name_title = customtkinter.CTkLabel(self._name_view_frame, text='Nombre:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._name_title.grid(row=0, column=0, padx=(0, 10))

        self._name_entry_view = customtkinter.CTkEntry(self._name_view_frame, border_width=0, state='disabled', height=setting.HEIGHT)
        self._name_entry_view.grid(row=0, column=1, sticky=customtkinter.NSEW)

        self._dni_tlf_frame = customtkinter.CTkFrame(self._view_client_frame)
        self._dni_tlf_frame.configure(fg_color='transparent')
        self._dni_tlf_frame.grid(row=1, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._dni_title = customtkinter.CTkLabel(self._dni_tlf_frame, text='DNI:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._dni_title.grid(row=0, column=0, padx=(0,10))

        self._dni_entry_view = customtkinter.CTkEntry(self._dni_tlf_frame, border_width=0, state='disabled', height=setting.HEIGHT)
        self._dni_entry_view.grid(row=0, column=1, padx=(0,5), sticky=customtkinter.NSEW)

        self._tlf_title = customtkinter.CTkLabel(self._dni_tlf_frame, text='TLF:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._tlf_title.grid(row=0, column=2, padx=(0,10))

        self._tlf_entry_view = customtkinter.CTkEntry(self._dni_tlf_frame, border_width=0, state='disabled', height=setting.HEIGHT)
        self._tlf_entry_view.grid(row=0, column=3, sticky=customtkinter.NSEW)

        self.list = db()._locations_optionmenu(self.list)
        self._location_frame = customtkinter.CTkFrame(self._view_client_frame, fg_color='transparent')
        self._location_frame.grid(row=4, column=0, columnspan=2,pady=10, sticky=customtkinter.NSEW)
        self._location_view = customtkinter.CTkOptionMenu(self._location_frame, 
                                                values=self.list,
                                                width=200,
                                                state='disabled')
        self._location_view.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._location_view.set("Ubicación")
        self._location_reset = customtkinter.CTkButton(self._location_frame, text='', image=self._icon_reset, width=setting.HEIGHT, command=lambda:self._reset_location(self._location_view))
        self._location_reset.grid(row=0, column=1, padx=(5,0))

        self._mg_ip_frame = customtkinter.CTkFrame(self._view_client_frame)
        self._mg_ip_frame.configure(fg_color='transparent')
        self._mg_ip_frame.grid(row=5, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._mg_title = customtkinter.CTkLabel(self._mg_ip_frame, text='MG:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._mg_title.grid(row=0, column=0, padx=(0,10))

        self._mg_entry_view = customtkinter.CTkEntry(self._mg_ip_frame, border_width=0, state='disabled', height=setting.HEIGHT)
        self._mg_entry_view.grid(row=0, column=1, padx=(0,5), sticky=customtkinter.NSEW)

        self._ip_title = customtkinter.CTkLabel(self._mg_ip_frame, text='IP:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._ip_title.grid(row=0, column=2, padx=(0,10))

        self._ip_entry_view = customtkinter.CTkEntry(self._mg_ip_frame, border_width=0, state='disabled', height=setting.HEIGHT)
        self._ip_entry_view.grid(row=0, column=3, sticky=customtkinter.NSEW)


        self._email_frame = customtkinter.CTkFrame(self._view_client_frame, fg_color='transparent')
        self._email_frame.grid(row=6, column=0, columnspan=2, sticky=customtkinter.NSEW, pady=10)
        self._email_title = customtkinter.CTkLabel(self._email_frame, text='Email:', font=customtkinter.CTkFont( weight=setting.FONT))
        self._email_title.grid(row=0, column=0, padx=(0, 10))

        self._email_entry_view = customtkinter.CTkEntry(self._email_frame, border_width=0, state='disabled', height=setting.HEIGHT)
        self._email_entry_view.grid(row=0, column=1, sticky=customtkinter.NSEW)

        self._pay_state = customtkinter.CTkLabel(self._view_client_frame, text="Estado del Mes:", font=customtkinter.CTkFont( weight=setting.FONT))
        self._pay_state.grid(row=7, column=0, padx=10, sticky=customtkinter.W)

        self._radio_var_view = tk.StringVar()
        self._radiobutton_pay_view = customtkinter.CTkRadioButton(self._view_client_frame, text="Pago",
                                            variable= self._radio_var_view, value='Pago', state='disabled')
        self._radiobutton_earring_view = customtkinter.CTkRadioButton(self._view_client_frame, text="Pendiente",
                                            variable= self._radio_var_view, value='Pendiente', state='disabled')
        self._radiobutton_pay_view.grid(row=8, column=0)
        self._radiobutton_earring_view.grid(row=8, column=1)

        self._btn_frame = customtkinter.CTkFrame(self._view_client_frame)
        self._btn_frame.configure(fg_color='transparent')
        self._btn_frame.grid(row=9, column=0, pady=10, columnspan=2, sticky=customtkinter.NSEW)

        self._btn_delete_location = customtkinter.CTkButton(self._btn_frame, text="Borrar", width=60, fg_color=setting.WARNING, command=lambda:fv_parameters._delete_client())
        self._btn_delete_location.grid(row=0, column=0,  sticky=customtkinter.NSEW)
        self._btn_edit_location = customtkinter.CTkButton(self._btn_frame, text="Editar", width=60, fg_color=setting.EDIT_COLOR, command=lambda:fv_parameters._edit_client())
        self._btn_edit_location.grid(row=0, column=1,padx=5, sticky=customtkinter.NSEW)
        self._btn_save_location = customtkinter.CTkButton(self._btn_frame, text="Guardar", width=60, command=lambda:fv_parameters._save_edit())
        self._btn_save_location.grid(row=0, column=2, sticky=customtkinter.NSEW)

        self._message_client_view = customtkinter.CTkLabel(self._view_client_frame, text='')
        # self._message_client_view.grid(row=9, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._name_view_frame.columnconfigure(1, weight=1)
        self._email_frame.columnconfigure(1, weight=1)
        self._btn_frame.columnconfigure(0, weight=1)
        self._btn_frame.columnconfigure(1, weight=1)
        self._btn_frame.columnconfigure(2, weight=1)
        self._location_frame.columnconfigure(0, weight=1)

        self._mg_ip_frame.columnconfigure(1, weight=1)
        self._mg_ip_frame.columnconfigure(3, weight=2)
        self._dni_tlf_frame.columnconfigure(1, weight=1)
        self._dni_tlf_frame.columnconfigure(3, weight=2)
        self._view_client_frame.columnconfigure(1, weight=1)

        fv_parameters = vq(self._name_entry_view, self._dni_entry_view, self._tlf_entry_view, self._location_view, self._mg_entry_view, self._ip_entry_view,self._email_entry_view, self._radio_var_view, self.data_client, self._get_clients, self._message_client_view, self._entry_normal, self._entry_clear, self._entry_disabled, self._radiobutton_pay_view, self._radiobutton_earring_view, self._counter)

    def _create_client(self, wind):
        self._create_client_frame = customtkinter.CTkFrame(wind)
        self._create_client_frame.configure(fg_color='transparent')
        self._create_client_frame.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)

        self._data = customtkinter.CTkLabel(self._create_client_frame, text="Datos:", font=customtkinter.CTkFont( weight=setting.FONT))
        self._data.grid(row=1, column=0, padx=10, sticky=customtkinter.W)

        self._name_entry = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Nombre del cliente", height=setting.HEIGHT)
        self._name_entry.grid(row=2, column=0,columnspan=2, sticky=customtkinter.NSEW)
        self._name_entry.bind('<Button-1>', self._hide_message_client_frame)

        self._dni_entry_create = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="DNI", height=setting.HEIGHT)
        self._dni_entry_create.grid(row=3, column=0, pady=(10,0), padx=(0, 10), sticky=customtkinter.NSEW)
        self._dni_entry_create.bind('<Button-1>', self._hide_message_client_frame)


        self._tlf_entry_create = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Número telefonico", height=setting.HEIGHT)
        self._tlf_entry_create.grid(row=3, column=1, pady=(10,0), sticky=customtkinter.NSEW)
        self._tlf_entry_create.bind('<Button-1>', self._hide_message_client_frame)

        self.list = db()._locations_optionmenu(self.list)
        self._location_frame = customtkinter.CTkFrame(self._create_client_frame, fg_color='transparent')
        self._location_frame.grid(row=4, column=0, columnspan=2,pady=10, sticky=customtkinter.NSEW)
        self._location = customtkinter.CTkOptionMenu(self._location_frame, 
                                                    values=self.list,
                                                    width=200)
        self._location.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._location.set("Ubicación")
        self._location_reset = customtkinter.CTkButton(self._location_frame, text='', image=self._icon_reset, width=setting.HEIGHT, command=lambda:self._reset_location(self._location))
        self._location_reset.grid(row=0, column=1, padx=(5,0))


        self._megas_entry_create = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Megas", height=setting.HEIGHT)
        self._megas_entry_create.grid(row=5, column=0, padx=(0, 10), sticky=customtkinter.NSEW)
        self._megas_entry_create.bind('<Button-1>', self._hide_message_client_frame)


        self._ip_entry_create = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="IP", height=setting.HEIGHT)
        self._ip_entry_create.grid(row=5, column=1, sticky=customtkinter.NSEW)
        self._ip_entry_create.bind('<Button-1>', self._hide_message_client_frame)

        self._email_entry_create = customtkinter.CTkEntry(self._create_client_frame, placeholder_text="Correo Electronico", height=setting.HEIGHT)
        self._email_entry_create.grid(row=6, column=0, pady=(10,0), columnspan=2, sticky=customtkinter.NSEW)

        self._pay_create = customtkinter.CTkLabel(self._create_client_frame, text="Pago de mes:", font=customtkinter.CTkFont( weight=setting.FONT))
        self._pay_create.grid(row=7, column=0, padx=10, sticky=customtkinter.W)

        self._radio_var = tk.StringVar()
        self._radiobutton_pay = customtkinter.CTkRadioButton(self._create_client_frame, text="Pago",
                                            variable= self._radio_var, value='Pago')
        self._radiobutton_earring = customtkinter.CTkRadioButton(self._create_client_frame, text="Pendiente",
                                            variable= self._radio_var, value='Pendiente')
        self._radiobutton_pay.grid(row=8, column=0)
        self._radiobutton_earring.grid(row=8, column=1)


        self._btn_add_location = customtkinter.CTkButton(self._create_client_frame, text="Crear cliente", command=lambda: fc_parameters._create_client())
        self._btn_add_location.grid(row=9, column=0, columnspan=2, pady=10, sticky=customtkinter.NSEW)

        self._message_client_create = customtkinter.CTkLabel(self._create_client_frame, text='')
        # self._message_client_create.grid(row=9, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._location_frame.columnconfigure(0, weight=1)
        self._create_client_frame.columnconfigure(0, weight=1)
        self._create_client_frame.columnconfigure(1, weight=1)

        fc_parameters = qc(self._name_entry, self._dni_entry_create, self._tlf_entry_create, self._location, self._megas_entry_create, self._ip_entry_create, self._email_entry_create, self._radio_var, self._message_client_create, self._get_clients ,self._radiobutton_pay, self._radiobutton_earring, self._counter) # instance of the class that contains the functions

    def _location_settings_view(self, wind):

        self._location_settings_frame = customtkinter.CTkFrame(wind)
        self._location_settings_frame.configure(fg_color='transparent')
        self._location_settings_frame.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)
        
        self._location_entry = customtkinter.CTkEntry(self._location_settings_frame, placeholder_text='Introduce la ubicación', height=setting.HEIGHT)
        self._location_entry.grid(row=0, column=0, columnspan=2, pady=10, sticky=customtkinter.NSEW)
        self._location_entry.bind('<Button-1>', self._hide_message_location_frame)


        self._btn_location_settings = customtkinter.CTkFrame(self._location_settings_frame)
        self._btn_location_settings.configure(fg_color='transparent')

        self._btn_location_settings.grid(row=1, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._btn_delete_location = customtkinter.CTkButton(self._btn_location_settings, text='Borrar', width=60, command=lambda:fl_parameters._delete_location(), fg_color=setting.WARNING)
        self._btn_delete_location.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._btn_edit_location = customtkinter.CTkButton(self._btn_location_settings, text='Editar', width=60, fg_color=setting.EDIT_COLOR, command=lambda:fl_parameters._edit_location())
        self._btn_edit_location.grid(row=0, column=1, padx=5, sticky=customtkinter.NSEW)
        self._btn_save_location = customtkinter.CTkButton(self._btn_location_settings, text='Guardar', width=60, command=lambda:fl_parameters._save_location())
        self._btn_save_location.grid(row=0, column=2, sticky=customtkinter.NSEW)

        self._table_location = ttk.Treeview(self._location_settings_frame, columns=('location',), padding=[0], style="mystyle.Treeview")
        self._table_location.column('#0')
        self._table_location.heading('#0', text='Ubicación', anchor=tk.CENTER)
        self._table_location.column('#1', width=0, stretch=tk.NO)
        self._table_location.heading("#1",text="",anchor=tk.CENTER)

        self.yscroll = customtkinter.CTkScrollbar(self._location_settings_frame, command=self._table_location.yview)
        self.yscroll.grid(column=1, row=2, sticky='ns')

        self._table_location.configure(yscrollcommand=self.yscroll.set)
        self._table_location.grid(row=2, column=0, sticky=customtkinter.NSEW, pady=5)
        # self._table_location.bind('<<TreeviewSelect>>', self._hide_message_location_frame)

        self._message_location = customtkinter.CTkLabel(self._location_settings_frame, text='')
        # self._message_location.grid(row=3, column=0, columnspan=2, sticky=customtkinter.NSEW)

        self._btn_location_settings.columnconfigure(0, weight=1)
        self._btn_location_settings.columnconfigure(1, weight=1)
        self._btn_location_settings.columnconfigure(2, weight=1)
        self._location_settings_frame.columnconfigure(0, weight=1)

        fl_parameters = lq(self._location_entry, self._table_location, self._message_location)
        fl_parameters._get_locations()

# Nombre, ubicacion, IP, MG, Estado
    def _table(self, master):
        self.table = ttk.Treeview(master, columns=('name', 'location', 'IP', 'MG', 'state'), padding=[0,0,0,0,0], style="mystyle.Treeview")
        self.table.column('#0', width=0, stretch=tk.NO)
        self.table.heading("#0",text="",anchor=tk.CENTER)
        self.table.column('name', width=340, stretch=0)
        self.table.heading('name', text='Nombre')
        self.table.column('location',  width=330, stretch=0)
        self.table.heading('location', text='Ubicacion')
        self.table.column('IP', width=150, stretch=0)
        self.table.heading('IP', text='IP')
        self.table.column('MG', width=50, anchor=tk.CENTER, stretch=0)
        self.table.heading('MG', text='MG')
        self.table.column('state', width=90, anchor=tk.CENTER)
        self.table.heading('state', text='Estado')
        self.table.tag_configure('Pago', background=setting.CLIENT_PAY)
        self.table.tag_configure('Pendiente', background=setting.CLIENT_EARRING)
        self.yscroll = customtkinter.CTkScrollbar(master, command=self.table.yview)
        self.yscroll.grid(column=2, row=0, sticky='ns')

        self.table.configure(yscrollcommand=self.yscroll.set)
        self.table.grid(row=0, column=1, sticky=tk.NSEW, pady=10, padx=(10,0))
        self.table.bind('<<TreeviewSelect>>', self._client_view_data)
        self._get_clients()

    def _client_view_data(self, e):
        self.data_client.clear()
        try:
            self._message_client_view.grid_forget()

            self.data_client.append(self.table.item(self.table.selection())['values'][0])
            self.data_client.append(self.table.item(self.table.selection())['values'][7])
            client_name = self.table.item(self.table.selection())['values'][0]
            client_dni = self.table.item(self.table.selection())['values'][5]
            client_tlf = self.table.item(self.table.selection())['values'][6]
            client_megas = self.table.item(self.table.selection())['values'][3]
            client_ip = self.table.item(self.table.selection())['values'][2]
            client_location = self.table.item(self.table.selection())['values'][1]
            client_state = self.table.item(self.table.selection())['values'][4]
            client_email = self.table.item(self.table.selection())['values'][8]
            self._entry_normal()
            self._entry_clear()

            self._name_entry_view.insert(0, client_name)
            self._dni_entry_view.insert(0, client_dni)
            self._tlf_entry_view.insert(0, client_tlf)
            self._mg_entry_view.insert(0, client_megas)
            self._ip_entry_view.insert(0, client_ip)
            self._email_entry_view.insert(0, client_email)
            self._location_view.set(client_location)
            self._entry_disabled()


            if client_state == 'Pago':
                # self._radio_var_view = tk.StringVar(value='Pago')
                self._radiobutton_earring_view.configure(state='disabled')
                self._radiobutton_earring_view.deselect()
                self._radiobutton_pay_view.configure(state='normal')
                self._radiobutton_pay_view.select()
            elif client_state == 'Pendiente':
                # self._radio_var_view = 'Pendiente'
                self._radiobutton_pay_view.configure(state='disabled')
                self._radiobutton_pay_view.deselect()
                self._radiobutton_earring_view.configure(state='normal')
                self._radiobutton_earring_view.select()
            elif client_state == '':
                self._radiobutton_pay_view.configure(state='disabled')
                self._radiobutton_pay_view.deselect()
                self._radiobutton_earring_view.configure(state='disabled')
                self._radiobutton_earring_view.deselect()
        except Exception as e:
            self._message_client_view.grid(row=10, column=0, columnspan=2, sticky=customtkinter.NSEW)

    def _entry_normal(self):
        self._name_entry_view.configure(state='normal')
        self._dni_entry_view.configure(state='normal')
        self._tlf_entry_view.configure(state='normal')
        self._mg_entry_view.configure(state='normal')
        self._ip_entry_view.configure(state='normal')
        self._location_view.configure(state='normal')
        self._email_entry_view.configure(state='normal')
    
    def _entry_disabled(self):
        self._name_entry_view.configure(state='disabled')
        self._dni_entry_view.configure(state='disabled')
        self._tlf_entry_view.configure(state='disabled')
        self._mg_entry_view.configure(state='disabled')
        self._ip_entry_view.configure(state='disabled')
        self._location_view.configure(state='disabled')
        self._email_entry_view.configure(state='disabled')
    
    def _entry_clear(self):
        self._name_entry_view.delete(0, customtkinter.END)
        self._dni_entry_view.delete(0, customtkinter.END)
        self._tlf_entry_view.delete(0, customtkinter.END)
        self._mg_entry_view.delete(0, customtkinter.END)
        self._ip_entry_view.delete(0, customtkinter.END)
        self._email_entry_view.delete(0, customtkinter.END)
        
    def _reset_location(self, optionMenu):
        self.list = db()._locations_optionmenu(self.list)
        optionMenu.configure(values=self.list)

    def _hide_message_client_frame(self, e):
        self._message_client_create.grid_forget()

    def _hide_message_location_frame(self, e):
        self._message_location.grid_forget()

    def _get_clients(self):

        clients_table = self.table.get_children()
        for client in clients_table:
            self.table.delete(client)

        query = 'SELECT * FROM clients ORDER BY LOCATION DESC'
        clients = db()._connect_db(query)
        for client in clients:
            self.table.insert('', 0, text=client[0] , values=[client[1], client[4],client[6], client[5], client[7], client[2], client[3], client[0], client[8]], tags=(client[7],))

    def _counter(self):
        counter_client = 0
        counter_mg = 0
        counter_mg_pay = 0
        counter_mg_earring = 0

        for i in db()._all_clients():
            counter_client += 1
            counter_mg += i[5]
            if i[7] == 'Pago':
                counter_mg_pay += i[5]
            elif i[7] == 'Pendiente':
                counter_mg_earring += i[5]


        self._counter_client_state.configure(text=str(counter_client))
        self._counter_mg_state.configure(text=str(counter_mg))
        self._counter_mg_state_pay.configure(text=str(counter_mg_pay))
        self._counter_mg_state_earring.configure(text=str(counter_mg_earring))

    def _configure_self(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, minsize=70)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, minsize=20)