# api/index.py
from http.server import BaseHTTPRequestHandler
import json
import pandas as pd

# ESEMPIO: qui carichi gli stessi dati che usavi in Streamlit
# Sostituisci con il tuo vero percorso / sorgente
CSV_PATH = "data/interventi.csv"  # esempio

def load_data():
    df = pd.read_csv(CSV_PATH)
    # qui puoi applicare eventuali pulizie/rename colonne
    return df

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            df = load_data()

            # ESEMPIO: restituisco solo alcune colonne / prime 50 righe
            data = df.head(50).to_dict(orient="records")

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))

        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
