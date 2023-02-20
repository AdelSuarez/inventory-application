import customtkinter
from components.NavBar import Navbar 

class Manager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.container = customtkinter.CTkFrame(self)
        self._configure_win()
        self._configure_self()
        self.container.pack(expand=True, fill=customtkinter.BOTH)

        self.my_frame = Navbar(master=self.container)

    def _configure_win(self):
        """Main window setting"""
        self.geometry('1200x700')
        self.minsize(width=1200, height=700)
        self.title('Sistema Inventario')


    def _configure_self(self):
        """Configuration of the upper menu, so that it is expandible"""
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, minsize=70)
        self.container.rowconfigure(1, weight=1)
        self.container.rowconfigure(2, minsize=20)