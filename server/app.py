from flask import Flask, request, jsonify
from flask_restful import Api, Resource

#create flask app
app = Flask(__name__)
#initialize
api = Api(app)

class Index(Resource):
    def get(self):
        return jsonify({'message': 'Hello World!'})
    
api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True, port=5555)
