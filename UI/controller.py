import flet as ft
from database.studente_DAO import ritorna_studenti, ritorna_studenti_corso, iscrivi_studente_corso
from database.corso_DAO import ritorna_corsi

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_hello(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""
        name = self._view.txt_name.value
        if name is None or name == "":
            self._view.create_alert("Inserire il nome")
            return
        self._view.txt_result.controls.append(ft.Text(f"Hello, {name}!"))
        self._view.update_page()

    def handle_cerca_iscritti(self, e):
        c_temp = self._view.dd.value
        if c_temp is None:
            self._view.create_alert("Selezionare un corso!")
            return
        nome_c, codins_c = c_temp.rsplit(maxsplit=1)
        studenti_tutti = ritorna_studenti()
        studenti_corsi_tutti = ritorna_studenti_corso()
        studenti_corsi = []
        for lista in studenti_corsi_tutti:
            if lista[1] == codins_c:
                studenti_corsi.append(lista[0])
        studenti = []
        for stud in studenti_tutti:
            for matricola in studenti_corsi:
                if stud.matricola == matricola:
                    studenti.append(stud)

        self._view.txt_result.controls.append(ft.Text(f"Ci sono {len(studenti)} iscritti al corso:"))
        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(f"\n{s}"))
        self._view.update_page()

    def handle_cerca_studente(self, e):
        matricola = self._view.tf1.value
        if matricola is None:
            self._view.create_alert("Scrivere una matricola!")
            return
        studenti = ritorna_studenti()
        for s in studenti:
            if int(s.matricola) == int(matricola):
                self._view.tf2.value = s.nome
                self._view.tf3.value = s.cognome
        if self._view.tf2.value == "" and self._view.tf2.value == "":
            self._view.create_alert("Matricola non trovata!")
        self._view.update_page()

    def handle_cerca_corsi(self, e):
        matricola = self._view.tf1.value
        if matricola is None:
            self._view.create_alert("Scrivere una matricola!")
            return
        lista_liste = ritorna_studenti_corso()
        lista_codins = []
        for matr, codins in lista_liste:
            if int(matr) == int(matricola):
                lista_codins.append(codins)
        if len(lista_codins) == 0:
            self._view.create_alert("Matricola non trovata!")
            return
        lista_codici = ritorna_corsi()
        for ins in lista_codins:
            for codice in lista_codici:
                if codice.codins == ins:
                    self._view.txt_result.controls.append(ft.Text(codice))
        self._view.update_page()

    def handle_iscrivi(self, e):
        c_temp = self._view.dd.value
        if c_temp is None:
            self._view.create_alert("Selezionare un corso!")
            return
        nome_c, codins_c = c_temp.rsplit(maxsplit=1)
        matricola = self._view.tf1.value
        if matricola is None:
            self._view.create_alert("Scrivere una matricola!")
            return
        studenti = ritorna_studenti()
        trovato = False
        for s in studenti:
            if int(s.matricola) == int(matricola):
                trovato = True
        if not trovato:
            self._view.create_alert("Matricola non esiste!")
            return
        stud_corsi = ritorna_studenti_corso()
        for stud, codins in stud_corsi:
            if stud == matricola and int(codins) == int(codins_c):
                self._view.create_alert("Matricola già iscritta al corso!")
                return

        iscrivi_studente_corso(int(matricola), codins_c)

        self._view.update_page()

