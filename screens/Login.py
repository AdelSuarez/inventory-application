import customtkinter
import os
from PIL import Image
import settings.settings as setting

class LoginScreen(customtkinter.CTkFrame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self._user_root = "admin"
        self._password_root = 'admin'
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
        self._user.bind('<Button-1>', self._hide_message_login)

        self._password = customtkinter.CTkEntry(self._inputs_frame, placeholder_text='Ingrese la contraseña', height=setting.HEIGHT, show='*')
        self._password.grid(row=2, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)
        self._password.bind('<Button-1>', self._hide_message_login)


        self._btn_login = customtkinter.CTkButton(self._inputs_frame, text='Ingresar',command=self._verification)
        self._btn_login.grid(row=3, column=0, pady=20)

        self._message_login = customtkinter.CTkLabel(self._inputs_frame, text='')

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

    def _verification(self):
        if len(self._user.get()) != 0:
            if len(self._password.get()) != 0:
                if (self._user.get() == self._user_root) and (self._password.get() == 'admin'):
                    print('valido')
                    self.manager.login_to_home()
                    self._user.delete(0, customtkinter.END)
                    self._password.delete(0, customtkinter.END)
                    self._hide_message_login()
                else:
                    self._message(self._message_login, 'Datos invalidos', setting.WARNING)
            else:
                self._message(self._message_login, 'Introduce la contaseña', setting.WARNING)
        else:
            self._message(self._message_login, 'Introduce el usuario', setting.WARNING)


    def _hide_message_login(self, e):
        self._message_login.grid_forget()
    
    def _message(self, message, text, color):
        message.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky=customtkinter.NSEW)
        message.configure(text=text, fg_color=color, corner_radius=60)

        
    def _configure_self(self):
        self.configure( fg_color=setting.BACKGROUND)
        self.grid(row=0, column=0, sticky=customtkinter.NSEW)
        self.columnconfigure(0, weight=1, minsize=330)
        self.columnconfigure(1, minsize=900)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
