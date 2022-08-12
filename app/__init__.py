from flask import Flask
from flask_bootstrap import Bootstrap
from config import DevConfig

bootstrap = Bootstrap()

def create_app(config_name):
    #initialize application
    app = Flask(__name__)

    #Setting app configuration
    app.config.from_object(config_options[config_name])

    #Initializing Flask Extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .requests import configure_request
    configure_request(app)


    return app

