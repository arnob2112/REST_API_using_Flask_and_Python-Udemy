from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identity
from resources.user import UserResgister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Arnob'
api = Api(app)
jwt = JWT(app, authentication, identity)


@app.before_first_request
def create_table():
    db.create_all()
    db.session.commit()


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserResgister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    app.run(port=5000, debug=True)
