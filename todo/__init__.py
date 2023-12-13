from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from . import todo

db=SQLAlchemy()



def create_app():
    app = Flask(__name__, template_folder='C:/Users/SOFTWARE/Desktop/todoLista/todo/templates')

#configuracion del proyectos
    app.config.from_mapping(
        debug = True,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///recargaya.db"
    )
    
    db.init_app(app)
#registrar bluprints
    from . import todo
    app.register_blueprint(todo.bp)
    from . import auth
    app.register_blueprint(auth.bp)
    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()
    
    return app

