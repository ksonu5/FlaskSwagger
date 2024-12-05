from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, doc='/swagger')  

ns = api.namespace('items', description='Items operations')

@ns.route('/<string:item_id>')
@api.response(404, 'Item not found')
class Item(Resource):
    def get(self, item_id):
        return {'item_id': item_id, 'name': 'Sample Item'}, 200

    def put(self, item_id):
        
        return {'message': 'Item updated', 'item_id': item_id}, 200

    def delete(self, item_id):
        
        return {'message': 'Item deleted', 'item_id': item_id}, 200

if __name__ == '__main__':
    app.run(debug=True)
