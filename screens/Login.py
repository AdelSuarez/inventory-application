import customtkinter
import os
from PIL import Image
from components.Login import Login
from components.Register import Register

class LoginScreen(customtkinter.CTkFrame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.container_login = customtkinter.CTkFrame(self)
        self._configure_self()
        self.container_login.pack(expand=True, fill=customtkinter.BOTH)

        self.manager = manager
        self._logo_init = customtkinter.CTkImage(Image.open(os.path.join("img/", "login_img.png")), size=(700, 700))
        
        self._img()

        self.frames = {}
        screens = (Login, Register)
        for f in screens:
            frame = f(self.container_login, self, self.manager)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky=customtkinter.NSEW)
        
        self.show_frame(Login)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def login_to_register(self):
        self.show_frame(Register)

    def register_to_login(self):
        self.show_frame(Login)

    def _img(self):
        self._img_frame = customtkinter.CTkFrame(self.container_login, corner_radius=0)
        self._img_frame.grid(row=0, column=1,sticky=customtkinter.NSEW)

        self._img_main = customtkinter.CTkLabel(self._img_frame, text='', image=self._logo_init)
        self._img_main.grid(row=0, column=0, sticky=customtkinter.NSEW)

        self._img_frame.columnconfigure(0, weight=1)
        self._img_frame.rowconfigure(0, weight=1)
        
    def _configure_self(self):
        # self.configure( fg_color=setting.BACKGROUND)
        # self.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self.container_login.columnconfigure(0, weight=1, minsize=330)
        self.container_login.columnconfigure(1, minsize=900)
        self.container_login.columnconfigure(1, weight=1)
        self.container_login.rowconfigure(0, weight=1)
