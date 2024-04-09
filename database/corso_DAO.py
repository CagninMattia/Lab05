# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


def ritorna_corsi():
    corsi = []
    cnx = get_connection()
    cursore = cnx.cursor()
    query = "SELECT * from corso"
    cursore.execute(query)
    rows = cursore.fetchall()
    for row in rows:
        (codins, crediti, nome, pd) = row
        c_temp = Corso(codins, crediti, nome, pd)
        corsi.append(c_temp)
    cnx.close()
    cursore.close()
    return corsi
