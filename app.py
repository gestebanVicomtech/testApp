from flask import Flask 
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



# Create the db and marshmallow objects
db = SQLAlchemy()
ma = Marshmallow()
CORS()

def create_app():
    # Initialize Flask app
    app= Flask(__name__)

    db_url= 'localhost:5432'
    db_name= 'testApp_db'
    db_user= 'testApp'
    db_password= 'testApp'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{db_user}:{db_password}@{db_url}/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db and marshmallow objects
    db.init_app(app)
    ma.init_app(app)

    # Register the blueprint
    from backend.routes.routes_battery import battery_route
    app.register_blueprint(battery_route)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
    