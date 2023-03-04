import customtkinter
from components.NavBar import Navbar
from components.NotificationBar import NotificationBar
from screens.Home import HomeScreen
customtkinter.set_appearance_mode("System")

class Manager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.container = customtkinter.CTkFrame(self)
        self._configure_window()
        self._configure_self()
        self.container.pack(expand=True, fill=customtkinter.BOTH)
        self._window()

    def _window(self):
        # main window widget structure
        self.navbar = Navbar(master=self.container)
        self.Home = HomeScreen(master=self.container)
        self.notification_bar = NotificationBar(master=self.container )

    def _configure_window(self):
        # Main window setting
        self.geometry('1230x735')
        self.minsize(width=1230, height=735)
        self.title('Control de clientes')


    def _configure_self(self):
        # Configuration of the upper menu, so that it is expandible
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, minsize=70)
        self.container.rowconfigure(1, weight=1,)
        self.container.rowconfigure(2, minsize=20)