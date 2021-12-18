from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_username(name)
        if store:
            return store.json(), 200
        return {"message": "Store not found."}, 400

    def post(self, name):
        if StoreModel.find_by_username(name):
            return {"message": "A store with this name '{}' already exists.".format(name)}, 404
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred."}, 500
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_username(name)
        if store:
            store.delete_from_db()
            return {"message": "Store deleted. "}
        else:
            return {"message": "Store is not register yet."}, 404


class StoreList(Resource):
    def get(self):
        return {"Stores": [store.json() for store in StoreModel.query.all()]}, 200



