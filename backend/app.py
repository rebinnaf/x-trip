from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
import os

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Swagger configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Trip Experience API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    transport = db.Column(db.String(100))
    location = db.Column(db.String(100))
    hotel = db.Column(db.String(100))
    attractions = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'transport': self.transport,
            'location': self.location,
            'hotel': self.hotel,
            'attractions': self.attractions
        }

@app.route('/api/trips', methods=['GET'])
def get_trips():
    trips = Trip.query.all()
    return jsonify([trip.to_dict() for trip in trips])

@app.route('/api/trips/<int:trip_id>', methods=['GET'])
def get_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    return jsonify(trip.to_dict())

@app.route('/api/trips', methods=['POST'])
def create_trip():
    data = request.json
    new_trip = Trip(
        name=data['name'],
        description=data.get('description'),
        transport=data.get('transport'),
        location=data.get('location'),
        hotel=data.get('hotel'),
        attractions=data.get('attractions')
    )
    db.session.add(new_trip)
    db.session.commit()
    return jsonify(new_trip.to_dict()), 201

@app.route('/api/trips/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    data = request.json
    
    trip.name = data.get('name', trip.name)
    trip.description = data.get('description', trip.description)
    trip.transport = data.get('transport', trip.transport)
    trip.location = data.get('location', trip.location)
    trip.hotel = data.get('hotel', trip.hotel)
    trip.attractions = data.get('attractions', trip.attractions)
    
    db.session.commit()
    return jsonify(trip.to_dict())

@app.route('/api/trips/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    trip = Trip.query.get_or_404(trip_id)
    db.session.delete(trip)
    db.session.commit()
    return '', 204

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 