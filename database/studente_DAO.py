# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


def ritorna_studenti_corso():
    studenti_corso = []
    cnx = get_connection()
    cursore = cnx.cursor()
    query = "SELECT * from iscrizione"
    cursore.execute(query)
    rows = cursore.fetchall()
    for row in rows:
        (matricola, codins) = row
        studenti_corso.append([matricola, codins])
    cnx.close()
    cursore.close()
    return studenti_corso


def ritorna_studenti():
    studenti = []
    cnx = get_connection()
    cursore = cnx.cursor()
    query = "SELECT * from studente"
    cursore.execute(query)
    rows = cursore.fetchall()
    for row in rows:
        (matricola, nome, cognome, cds) = row
        s_temp = Studente(matricola, nome, cognome, cds)
        studenti.append(s_temp)
    cnx.close()
    cursore.close()
    return studenti


def iscrivi_studente_corso(matr, codins):
    cnx = get_connection()
    cursore = cnx.cursor()
    query = "INSERT INTO iscrizione (matricola, codins) VALUES (%s, %s)"
    cursore.execute(query, (matr, codins))
    cnx.commit()
    cnx.close()
    cursore.close()


