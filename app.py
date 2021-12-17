from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identity
from section6.code.resources.user import UserResgister
from section6.code.resources.item import Item, ItemList
from section6.code.resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Arnob'
api = Api(app)
jwt = JWT(app, authentication, identity)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResgister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
