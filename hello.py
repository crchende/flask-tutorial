from flask import Flask

app = Flask(__name__)   # instantiere obiect aplicatie
                        # primeste parametru numele fisierului fara py

@app.route('/')
def index():
    ret = "Salutare <br/>"
    ret += "Variabile disponibile in Python: <br/>"
    ret += "__name__ = " + __name__ + "<br/>" # doar numele fisierului - fara py
    ret += "__file__ = " + __file__ + "<br/>" # cale absoluta + nume fisier si extensie
    return ret