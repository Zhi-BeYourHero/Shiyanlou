from flask import Flask, render_template
from simpledu.models import db, Course
from simpledu.config import configs
from flask_migrate import Migrate

def create_app(config):

    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    #初始化SQLAlchemy
    db.init_app(app)
    register_blueprints(app)
    Migrate(app,db)
    return app

def register_blueprints(app):
    from .handlers import course,front,admin
    app.register_blueprint(course)
    app.register_blueprint(front)
    app.register_blueprint(admin)
   
