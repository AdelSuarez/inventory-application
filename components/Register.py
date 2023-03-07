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

        self._title_register = customtkinter.CTkFrame(self._register_frame, fg_color='transparent')
        self._title_register.grid(row=0, column=0, sticky=customtkinter.NSEW, columnspan=2, padx=10, pady=10)

        self._btn_back = customtkinter.CTkButton(self._title_register, text='', image=self._icon_arrow, width=40, fg_color='transparent', hover=False, command=lambda:self.manager.register_to_login())
        self._btn_back.grid(row=0, column=0)

        self._title = customtkinter.CTkLabel(self._title_register, text='Usuario Nuevo',font=customtkinter.CTkFont(family='Oswald', size=18, weight="bold"))
        self._title.grid(row=0, column=1, columnspan=2, sticky=customtkinter.NSEW)

        self._title_register.columnconfigure(1, weight=1)
        self._register_frame.rowconfigure(0, weight=1)
        self._register_frame.columnconfigure(0, weight=1)



    


