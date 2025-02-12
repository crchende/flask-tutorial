from flask import Flask

def create_app():

    app = Flask(__name__)
    print("__", __name__)
    @app.route('/')
    def hello():
        return "SALUT"
    
    return app
    '''
    #app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__, instance_relative_config=True) 
    # incarca fisierul de configurare din directorul 'instance', nu din root
    # fara acest parametru, se va incerca incarcarea config.py din 'flaskr'
    # cu acesta - din directorul 'instance' care este in afara 'flaskr'
    print("app.instance_path:", app.instance_path)
    print("app.root_path:    ", app.root_path)

    app.config.from_pyfile('config.py', silent=False)
    print(app.config)
    '''