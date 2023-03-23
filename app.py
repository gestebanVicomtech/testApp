from flask import Flask 
from flask_cors import CORS
from config import db

 
# Initialize Flask app
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://testApp:testApp@localhost/testApp_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask extensions

CORS(app)


def createBlueprints():
    # Register the blueprint
    from routes.routes_battery import battery_route
    app.register_blueprint(battery_route)
    from routes.routes_batteryFamily import batteryFamily_route
    app.register_blueprint(batteryFamily_route)
    from routes.routes_test import test_route
    app.register_blueprint(test_route)

def createApp():
    db.init_app(app)

if __name__ == '__main__':
    createApp()
    app.app_context().push()
    createBlueprints()
    db.create_all()
    app.run(debug=True)
    
    