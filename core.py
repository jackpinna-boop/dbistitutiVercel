# core.py
import pandas as pd

CSV_PATH = "data/interventi.csv"  # metti il percorso giusto

def get_interventi_filtrati(tipo=None, comune=None):
    df = pd.read_csv(CSV_PATH)

    # ESEMPI DI FILTRI – sostituisci con i tuoi filtri reali
    if tipo is not None:
        df = df[df["TIPO_INTERVENTO"] == tipo]
    if comune is not None:
        df = df[df["COMUNE"] == comune]

    return df
