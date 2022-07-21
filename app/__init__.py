from flask import Flask
from app.controllers.quality_image import quality_image_bp
from app.controllers.classification import classification_bp
from app.controllers.detection import detection_bp
from app.services import init_models
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

CONFIG_FILENAME = "config" # TODO: move to os env
URL_PREFIX = "/coreai/v1"


def create_app():
    app = Flask(__name__)
    app.config.from_object(CONFIG_FILENAME)
    app.secret_key = app.config["SECRET_KEY"]
    
    app.models = init_models(app.config["MODELS_CONFIG"])
        
    # Import a module / component using its blueprint handler variable
    app.register_blueprint(quality_image_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(classification_bp, url_prefix=URL_PREFIX)
    app.register_blueprint(detection_bp, url_prefix=URL_PREFIX)
    return app