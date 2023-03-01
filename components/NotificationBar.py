import customtkinter
import settings.settings as setting

class NotificationBar(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid(row=2, column=0, columnspan=2,  sticky=customtkinter.NSEW)
        self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)

        self.configure(corner_radius=0)
        self._create_widgets()

    def _create_widgets(self):

        self._bar_frame = customtkinter.CTkFrame(self)
        self._bar_frame.configure( fg_color=setting.BACKGROUND, corner_radius=0)
        self._bar_frame.grid(row=0, column=0, sticky=customtkinter.NSEW)

        self._user = customtkinter.CTkLabel(master=self._bar_frame, text='Developer')
        self._user.grid(row=0, column=0, padx=20, sticky=customtkinter.W)
        self._version =customtkinter.CTkLabel(master=self._bar_frame, text='v0.1.5')
        self._version.grid(row=0, column=1, padx=20, sticky=customtkinter.E)

        self._bar_frame.columnconfigure(0, weight=1)
        self._bar_frame.columnconfigure(1, weight=1)


        
