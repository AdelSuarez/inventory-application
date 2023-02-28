import customtkinter
from components.NavBar import Navbar
from components.NotificationBar import NotificationBar
from screens.Home import HomeScreen
customtkinter.set_appearance_mode("System")

class Manager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.container = customtkinter.CTkFrame(self)
        self._configure_win()
        self._configure_self()
        self.container.pack(expand=True, fill=customtkinter.BOTH)
        self._win()

    def _win(self):
        self.navbar = Navbar(master=self.container)
        self.Home = HomeScreen(master=self.container)
        self.notification_bar = NotificationBar(master=self.container )

    def _configure_win(self):
        """Main window setting"""
        self.geometry('1200x700')
        self.minsize(width=1200, height=700)
        self.title('Control de clientes')


    def _configure_self(self):
        """Configuration of the upper menu, so that it is expandible"""
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, minsize=70)
        self.container.rowconfigure(1, weight=1,)
        self.container.rowconfigure(2, minsize=20)