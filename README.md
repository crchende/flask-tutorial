# flask-tutorial
Flaskr tutorial from: https://flask.palletsprojects.com/en/stable/tutorial/

# Cuprins

- [i. Unelte necesare](#i-unelte-necesare)

- [ii. Executia aplicatiei flask](#ii-executia-aplicatiei-flask)

- [1. Aplicatie simpla cu un fisier](#1-aplicatie-simpla-cu-un-fisier)

- [2. Aplicatia in director cu 'application factory'](#2-aplicatia-in-director-cu-application-factory)
  - [2.1. Configurarea aplicatiei in `application factory`](#21-configurarea-aplicatiei-in-application-factory)

### i. Unelte necesare
- virtual environment - instalat in directorul flask-tutorial

        python3 -m venv .venv  # creaza directorul .venv si instaleaza 
                               # python si pachetele de baza pentru python


- flask instalat in proiect

        pip install flask


### ii. Executia aplicatiei flask
[Cuprins](#cuprins)

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

# 1. Aplicatie simpla cu un fisier
[Cuprins](#cuprins)

- director de lucru: `flask-tutorial`
- fisier python care creaza o aplicatie flask: `hello.py`
  
        app = Flask(__name__) # argumentul __name__ este pus la dispozitie 
                              # de Python si reprezinta chiar numele fisierului, 
                              # fara extensie
                              # Flask trebuie sa stie ce sa importe - i se furnizeaza
                              # acest lucru prin intermediul parametrului __name__

- aplicatia contine rute care returneaza ce se afiseaza in pagina web
  
        @app.route('/')
        def index():
            return <un text>

# 2. Aplicatia in director cu 'application factory'

- se creaza directorul `flaskr` - pentru aplicatie.
- in director se creaza fisierul `__init__.py` care in varianta cea mai simpla are continutul:

        from flask import Flask

        def create_app():
            app = Flask(__name__) # __name__ = numele modulului python curent
                              # in acest caz - chiar directorul 'flaskr'
                              # care are in el fisierul __init__.py
            print("__name__ =", __name__) 
            @app.route('/')
            def hello():
                return "SALUT"
        
            return app

- `create_app` este 'application factory'. programul `flask` cauta in `__init__.py` si executa aceasta functie daca i se da ca `--app` un director - `flaskr` in cazul de fata. De vazut exemplul de executie a aplicatiei de mai jos.

- in aceste exemplu, in interiorul `application factory` avem definita si ruta si metoda `view` (@app.route ...).

- executia aplicatiei - din terminal, si directorul `flask-tutorial`, directorul parinte al directorului `flaskr`
  
        cip@cipasus:~/programare/git/flask-tutorial$ flask --app flaskr run --debug
         * Serving Flask app 'flaskr'
         * Debug mode: on
        WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
         * Running on http://127.0.0.1:5000
        Press CTRL+C to quit
         * Restarting with stat
         __name__ =  flaskr
         * Debugger is active!
         * Debugger PIN: 879-666-817

## 2.1. Configurarea aplicatiei in `application factory`
