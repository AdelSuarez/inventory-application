import tkinter as tk
import customtkinter
import threading
import time
# import datetime

import settings.settings as setting


class Navbar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        customtkinter.CTkFrame.__init__( self, master, *args, **kwargs)
        self._master= master 
        # Settings Frame
        self.configure( fg_color=setting.BACKGROUND, corner_radius=0)
        self.grid(row=0, column=0, sticky=customtkinter.NSEW, columnspan=2)

        # initiator of widget
        self._init_widget()
        
        # create the background thread
        self.timer_runs = threading.Event()
        self.timer_runs.set()
        t = threading.Thread(target=self.timer, args=(self.timer_runs,))
        t.start()

        # end time background task
        self.master.bind('<Destroy>', self._finish_execution)

        # TODO
        # The variables year and month are going to be used to create a function that restores the values ​​of the payment of the clients every month
        # ano = datetime.datetime.today().year
        # mes = datetime.datetime.today().month


    def _init_widget(self):

        self._navbar_frama = customtkinter.CTkFrame(self, fg_color='transparent')
        self._navbar_frama.pack(side = tk.TOP,
            fill = tk.BOTH, 
            expand = True)

        self._title_app = customtkinter.CTkLabel(self._navbar_frama, text="CONTROL DE CLIENTES", font=customtkinter.CTkFont(family='Oswald', size=18, weight="bold"))
        self._title_app.grid(row=0, column=0, padx=(20,0), sticky=tk.W)
        self._hour = customtkinter.CTkLabel(self._navbar_frama, text="", font=customtkinter.CTkFont(family='Oswald', size=18, weight="bold"))
        self._hour.grid(row=0, column=1, padx=(0,20))

        # settings frame
        self._navbar_frama.columnconfigure(0, weight=1)
        self._navbar_frama.rowconfigure(0, weight=1)
        self._navbar_frama.rowconfigure(0, weight=1)        


    def _finish_execution(self, e):
        self.timer_runs.clear()
        

    def timer(self ,timer_runs):
        while timer_runs.is_set():
            time_local = time.localtime()
            time_str = time.strftime("%d-%m-%Y %H:%M", time_local)
            self._hour.configure(text=time_str)
            time.sleep(10)