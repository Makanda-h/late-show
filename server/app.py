from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from models import db
from flask_migrate import Migrate

#create flask app
app = Flask(__name__)

#configure app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

#initialize
api = Api(app)

class Index(Resource):
    def get(self):
        return jsonify({'message': 'Hello World!'})
    
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
