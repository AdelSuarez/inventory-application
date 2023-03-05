import customtkinter
import os
from PIL import Image
import settings.settings as setting

class LoginScreen(customtkinter.CTkFrame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self._logo_init = customtkinter.CTkImage(Image.open(os.path.join("img/", "login_img.png")), size=(700, 700))
        self._configure_self()
        self._init_widget()
        self._img()


    def _init_widget(self):
        self._frame_main = customtkinter.CTkFrame(master=self,fg_color='transparent',corner_radius=0)
        self._frame_main.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self._login()

        self._frame_main.columnconfigure(0, weight=1)
        self._frame_main.rowconfigure(0, weight=1)

    
    def _login(self):
        self._login_frame = customtkinter.CTkFrame(self._frame_main, fg_color='transparent')
        self._login_frame.grid(row=0, column=0,sticky=customtkinter.NSEW)

        self._title_app = customtkinter.CTkLabel(self._login_frame, text='CONTROL DE CLIENTE', font=customtkinter.CTkFont(family='Oswald', size=22, weight="bold"))
        self._title_app.grid(row=0, column=0, pady=80, sticky=customtkinter.N)

        self._inputs_frame = customtkinter.CTkFrame(self._login_frame, fg_color='transparent')
        self._inputs_frame.grid(row=1, column=0,sticky=customtkinter.NSEW)

        self._user = customtkinter.CTkEntry(self._inputs_frame, placeholder_text='Ingrese el usuario', height=setting.HEIGHT)
        self._user.grid(row=1, column=0, padx=20, pady=(40,0), sticky=customtkinter.NSEW)

        self._password = customtkinter.CTkEntry(self._inputs_frame, placeholder_text='Ingrese la contraseña', height=setting.HEIGHT)
        self._password.grid(row=2, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)

        self._btn_login = customtkinter.CTkButton(self._inputs_frame, text='Ingresar',command=lambda:self.manager.login_to_home())
        self._btn_login.grid(row=3, column=0, pady=20)

        self._register_app = customtkinter.CTkLabel(self._login_frame, text='Registrar')
        self._register_app.grid(row=2, column=0, sticky=customtkinter.S)

        # Settings frame
        self._inputs_frame.columnconfigure(0, weight=1)
        self._login_frame.columnconfigure(0, weight=1)
        self._login_frame.rowconfigure(1, weight=1)
        # self._login_frame.rowconfigure(2, weight=1)



    def _img(self):
        self._img_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self._img_frame.grid(row=0, column=1,sticky=customtkinter.NSEW)

        self._img_main = customtkinter.CTkLabel(self._img_frame, text='', image=self._logo_init)
        self._img_main.grid(row=0, column=0, sticky=customtkinter.NSEW)

        self._img_frame.columnconfigure(0, weight=1)
        self._img_frame.rowconfigure(0, weight=1)

        
    def _configure_self(self):
        self.configure( fg_color=setting.BACKGROUND)
        self.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self.columnconfigure(0, weight=1, minsize=330)
        self.columnconfigure(1, minsize=900)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
