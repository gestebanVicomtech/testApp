from flask import Flask 
from routes.routes_battery import battery_route
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

 
# Initialize Flask app
app= Flask(__name__)

db_url= 'localhost:5432'
db_name= 'testApp_db'
db_user= 'testApp'
db_password= 'testApp'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{db_user}:{db_password}@{db_url}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask extensions
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)


# Register the blueprint
app.register_blueprint(battery_route)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    
    