from flask import Flask

from app import routes

def create_app(config_name):

    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    # app.config.from_object(config_module)
	
    app.register_blueprint(routes.blueprint)
	
    return app