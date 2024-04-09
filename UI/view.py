import flet as ft

from database.corso_DAO import ritorna_corsi


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_cerca_iscritti = None
        self.txt_result = None
        self.txt_container = None
        self.dd = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("Hello World", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with some controls
        # text field for the name
        self.dd = ft.Dropdown(
            width=700
        )
        self.fill_corso()

        # button for the "hello" reply
        self.btn_cerca_iscritti = ft.ElevatedButton(text="Cerca Iscritti", on_click=self._controller.handle_cerca_iscritti, )
        ###Da cambiare da self._controller.handle_hello a self._controller.handle_cerca_iscritti
        row1 = ft.Row([self.dd, self.btn_cerca_iscritti],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)

        self.tf1 = ft.TextField(label="Matricola")
        self.tf2 = ft.TextField(read_only=True, label="Nome")
        self.tf3 = ft.TextField(read_only=True, label="Cognome")

        row2 = ft.Row([self.tf1, self.tf2, self.tf3],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self.btn_cerca_studente = ft.ElevatedButton(text="Cerca Studente", on_click=self._controller.handle_cerca_studente)
        self.btn_cerca_corsi = ft.ElevatedButton(text="Cerca Corsi", on_click=self._controller.handle_cerca_corsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi", on_click=self._controller.handle_iscrivi)
        ### Da modificare anche questi bottoni

        row3 = ft.Row([self.btn_cerca_studente, self.btn_cerca_corsi, self.btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

    def fill_corso(self):
        corsi = ritorna_corsi()
        for corso in corsi:
            self.dd.options.append(ft.dropdown.Option(corso))
