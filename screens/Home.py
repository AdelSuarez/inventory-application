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

        self.title_label = customtkinter.CTkLabel(self._controller, text="Crear Cliente", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky=customtkinter.W)

        self.date = customtkinter.CTkLabel(self._controller, text="Datos:", font=customtkinter.CTkFont( weight="bold"))
        self.date.grid(row=1, column=0, padx=30, sticky=customtkinter.W)

        self.name_entry = customtkinter.CTkEntry(self._controller, placeholder_text="Nombre del cliente", height=40)
        self.name_entry.focus()
        self.name_entry.grid(row=2, column=0,columnspan=2, padx=20, sticky=customtkinter.NSEW)

        self.dni_entry = customtkinter.CTkEntry(self._controller, placeholder_text="DNI", height=40)
        self.dni_entry.grid(row=3, column=0, pady=(10,0), padx=(20, 10), sticky=customtkinter.NSEW)

        self.tlf_entry = customtkinter.CTkEntry(self._controller, placeholder_text="Numero telefonico", height=40)
        self.tlf_entry.grid(row=3, column=1, pady=(10,0), padx=(0, 20), sticky=customtkinter.NSEW)

        self.locatiom = customtkinter.CTkOptionMenu(self._controller, 
                                                values=["option 1", "option 2"],
                                                width=250)
        self.locatiom.grid(row=4, column=1,pady=10,padx=(0,20), sticky=customtkinter.W)
        self.locatiom.set("option 2")

        self.btn_add_location = customtkinter.CTkButton(self._controller, text="Agregar", command=self._add_location)
        self.btn_add_location.grid(row=4, column=0,pady=10, padx=(20,10), sticky=customtkinter.E)

        self.megas_entry = customtkinter.CTkEntry(self._controller, placeholder_text="Megas", height=40)
        self.megas_entry.grid(row=5, column=0, padx=(20, 10), sticky=customtkinter.NSEW)

        self.ip_entry = customtkinter.CTkEntry(self._controller, placeholder_text="IP", height=40)
        self.ip_entry.grid(row=5, column=1, padx=(0, 20), sticky=customtkinter.NSEW)

        self._controller.columnconfigure(0, weight=1)
        self._controller.columnconfigure(1, weight=1)

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
