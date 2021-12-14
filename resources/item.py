from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from section6.code.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot left blank')
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every items need a store id.')

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_username(name)
        if item:
            return item.json(), 200
        return {"message": "Item not found."}, 404

    def post(self, name):
        if ItemModel.find_by_username(name):
            return {"message": "An item with name '{}' already exists".format(name)}, 404

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}

        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_username(name)
        if item:
            item.delete_from_db()
        return {"message": "item deleted."}

    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_username(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": [x.json() for x in ItemModel.query.all()]}
