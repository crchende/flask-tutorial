# flask-tutorial
Flaskr tutorial from: https://flask.palletsprojects.com/en/stable/tutorial/

# Varianta cea mai simpla de aplicatie
- director de lucru: `flask-tutorial`
- fisier python care creaza o aplicatie flask: `hello.py`
  
        app = Flask(__name__) # argumentul __name__ este pus la dispozitie 
                              # de Python si reprezinta chiar numele fisierului, 
                              # fara extensie

- aplicatia contine rute care returneaza ce se afiseaza in pagina web
  
        @app.route('/')
        def index():
            return <un text>



## Unelte care trebuie instalate pentru aplicatia flask:
- virtual environment - instalat in directorul flask-tutorial

        python3 -m venv .venv  # creaza directorul .venv si instaleaza 
                               # python si pachetele de baza pentru python


- flask instalat in proiect

        pip install flask


# Executia aplicatiei flask

- din linia de comanda, cu specificarea explicita a aplicatiei: https://flask.palletsprojects.com/en/stable/cli/

        cd flask-tutorial # daca nu sunteti deja in directorul flask-tutorial
        
        flask --app hello --debug run

        --app hello       Numele aplicatiei. trebuie sa fie numele fisierului fara extensie
                          Python-ul incearca sa importe numele dat ca parametru.

        --debug           Pornirea aplicatiei in modul debug. Foarte util la dezvoltare
                          Dupa fiecare modificare a fisierelor .py, aplicatia se reincarca.

        run               Comanda de executie - flask va executa aplicatia primita ca parametru

- din linia de comanda - cu aplicatia luata din variabile de mediu: https://flask.palletsprojects.com/en/stable/cli/#environment-variables-from-dotenv

- LINUX:

        export FLASK_APP=hello
        export FLASK_RUN_PORT=5012

        flask run      # va porni aplicatia hello pe portul 5012
                       # nu mai este nevoie sa se specifice datale in linia de comanda
                       # flask le ia din env

        NOTA: se pot adauga in .bashrc (liniile de mai sus)

- WINDOWS CMD:
  
        > set FLASK_RUN_PORT=8000
        > flask run
        * Running on http://127.0.0.1:8000/
  
- WINDOWS Powershell:

        > $env:FLASK_RUN_PORT = 8000
        > flask run
         * Running on http://127.0.0.1:8000/