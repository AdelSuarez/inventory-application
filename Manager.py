import customtkinter
from components.NavBar import Navbar
from components.NotificationBar import NotificationBar
from screens.Home import HomeScreen
from screens.Login import LoginScreen
customtkinter.set_appearance_mode("System")

class Manager(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.container = customtkinter.CTkFrame(self)
        self._configure_window()
        self.container.pack(expand=True, fill=customtkinter.BOTH)

        self.frames = {}
        screens = (LoginScreen, HomeScreen)
        for f in screens:
            frame = f(self.container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky=customtkinter.NSEW)
        
        self.show_frame(LoginScreen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def login_to_home(self):
        self.show_frame(HomeScreen)
    
    def sign_off(self):
        self.show_frame(LoginScreen)


    def _home_screen(self):
        # main window widget structure
        self._configure_home_screen()
        self.navbar = Navbar(master=self.container)
        self.Home = HomeScreen(master=self.container)
        self.notification_bar = NotificationBar(master=self.container )

    def _configure_window(self):
        # Main window setting
        self.geometry('1230x735')
        self.minsize(width=1230, height=735)
        self.title('Control de clientes')
        self.container.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
