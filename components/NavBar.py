import customtkinter
import settings.settings as setting

class Navbar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        customtkinter.CTkFrame.__init__( self, master, *args, **kwargs)
        self._master= master
        self.configure( fg_color=setting.BACKGROUND, corner_radius=0)
        self.grid(row=0, column=0, sticky=customtkinter.NSEW, columnspan=2)

        self.title = customtkinter.CTkLabel(master=self, text="SISTEMA DE INVENTARIO", font=customtkinter.CTkFont(family='Oswald', size=18, weight="bold"))
        self.title.pack(side=customtkinter.LEFT, padx=20)