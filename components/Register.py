import customtkinter
import settings.settings as setting
import os
from PIL import Image 

class Register(customtkinter.CTkFrame):
    def __init__(self, parent, manager_login, manager_main):
        super().__init__(parent)
        self._icon_arrow = customtkinter.CTkImage(Image.open(os.path.join("img/", "arrow_back.png")), size=(28, 28))
        self.manager_main = manager_main
        self.manager = manager_login
        self._init_widget()


        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    
    def _init_widget(self):
        self._register_frame = customtkinter.CTkFrame(self, fg_color=setting.BACKGROUND, corner_radius=0)
        self._register_frame.grid(row=0, column=0,sticky=customtkinter.NSEW)

        # ----- BACK
        self._title_register = customtkinter.CTkFrame(self._register_frame, fg_color='transparent')
        self._title_register.grid(row=0, column=0, sticky=customtkinter.NSEW, columnspan=2, padx=10, pady=10)

        self._btn_back = customtkinter.CTkButton(self._title_register, text='', image=self._icon_arrow, width=40, fg_color='transparent', hover=False, command=lambda:self.manager.register_to_login())
        self._btn_back.grid(row=0, column=0)

        self._title = customtkinter.CTkLabel(self._title_register, text='Usuario Nuevo',font=customtkinter.CTkFont(family='Oswald', size=18, weight="bold"), fg_color='transparent')
        self._title.grid(row=0, column=1, columnspan=2)

        # ------- Data
        self._frame_data_register = customtkinter.CTkFrame(self._register_frame, fg_color='transparent')
        self._frame_data_register.grid(row=1, column=0, sticky=customtkinter.NSEW, columnspan=2)

        self._title_data = customtkinter.CTkLabel(self._frame_data_register, text='Datos personales',font=customtkinter.CTkFont(family='Oswald', size=14), fg_color='transparent')
        self._title_data.grid(row=0, column=0, padx=(20,0), sticky=customtkinter.W)

        self._frame_name_complete = customtkinter.CTkFrame(self._frame_data_register, fg_color='transparent')
        self._frame_name_complete.grid(row=1, column=0, sticky=customtkinter.NSEW, columnspan=2)
        self._name = customtkinter.CTkEntry(self._frame_name_complete, placeholder_text='Nombre', height=setting.HEIGHT)
        self._name.grid(row=0, column=0, padx=(20,10), pady=(5,0), sticky=customtkinter.NSEW)
        self._last_name = customtkinter.CTkEntry(self._frame_name_complete, placeholder_text='Apellido', height=setting.HEIGHT)
        self._last_name.grid(row=0, column=1, padx=(0,20), pady=(5,0), sticky=customtkinter.NSEW)

        self._user = customtkinter.CTkEntry(self._frame_data_register, placeholder_text='Usuario', height=setting.HEIGHT)
        self._user.grid(row=2, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)
        self._password = customtkinter.CTkEntry(self._frame_data_register, placeholder_text='Contraseña', height=setting.HEIGHT)
        self._password.grid(row=3, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)
        self._verify_password = customtkinter.CTkEntry(self._frame_data_register, placeholder_text='Verifica la contraseña', height=setting.HEIGHT)
        self._verify_password.grid(row=4, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)

        self._quesk = customtkinter.CTkLabel(self._frame_data_register, text='Preguntas de seguridad',font=customtkinter.CTkFont(family='Oswald', size=14), fg_color='transparent')
        self._quesk.grid(row=5, column=0, columnspan=2, pady=(10,5))
        self._p1 = customtkinter.CTkEntry(self._frame_data_register, placeholder_text='Pregunta 1', height=setting.HEIGHT)
        self._p1.grid(row=6, column=0, padx=20, sticky=customtkinter.NSEW)
        self._p2 = customtkinter.CTkEntry(self._frame_data_register, placeholder_text='Pregunta 2', height=setting.HEIGHT)
        self._p2.grid(row=7, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)
        self._p3 = customtkinter.CTkEntry(self._frame_data_register, placeholder_text='Pregunta 3', height=setting.HEIGHT)
        self._p3.grid(row=8, column=0, padx=20, pady=(10,0), sticky=customtkinter.NSEW)

        self._btn_create_user = customtkinter.CTkButton(self._frame_data_register, text='Crear usuario')
        self._btn_create_user.grid(row=9, column=0, pady=20)


        # ------- Settings frame
        self._title_register.columnconfigure(1, weight=1)

        self._frame_data_register.columnconfigure(0, weight=1)

        self._frame_name_complete.columnconfigure(0, weight=1)
        self._frame_name_complete.columnconfigure(1, weight=1)

        self._register_frame.rowconfigure(1, weight=1)
        self._register_frame.columnconfigure(0, weight=1)



    


