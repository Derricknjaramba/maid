from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  # Import Migrate

# Create instances for db and migrate
db = SQLAlchemy()
migrate = Migrate()  # Initialize the Migrate object

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize the db with the app inside create_app
    db.init_app(app)
    migrate.init_app(app, db)  # Link Flask-Migrate to app and db

    # Initialize API
    api = Api(app)

    # Import resources after db is initialized to avoid circular imports
    from app.resources import HouseHelpResource, ClientResource, AssignmentResource, PaymentResource
    api.add_resource(HouseHelpResource, '/househelps', '/househelp/<int:id>')
    api.add_resource(ClientResource, '/clients', '/client/<int:id>')
    api.add_resource(AssignmentResource, '/assignments', '/assignment/<int:id>')
    api.add_resource(PaymentResource, '/payments', '/payment/<int:id>')

    return app






