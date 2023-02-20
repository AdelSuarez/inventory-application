import customtkinter
import settings.settings as setting

class NotificationBar(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=2, column=0, sticky=customtkinter.NSEW, columnspan=2)
        self.configure( fg_color=setting.BACKGROUND, corner_radius=0)
        self._create_widgets()

    def _create_widgets(self):

        self._user = customtkinter.CTkLabel(master=self, text='Developer')
        self._user.grid(row=0, column=0, padx=20)
        # self._version =customtkinter.CTkLabel(master=self, text='V0.0.1')
        # self._user.grid(row=1, column=0, padx=20)
