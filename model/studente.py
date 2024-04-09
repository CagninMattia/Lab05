class Studente:
    def __init__(self, matricola, cognome, nome, cds):
        self.matricola = matricola
        self.cognome = cognome
        self.nome = nome
        self.cds = cds

    def __str__(self):
        return f"{self.nome}, {self.cognome} ({self.matricola})"
