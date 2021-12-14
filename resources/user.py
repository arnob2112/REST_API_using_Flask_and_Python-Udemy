import sqlite3
from flask_restful import Resource, reqparse
from section6.code.models.user import UserModel


class UserResgister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot left blank!")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot left blank!")

    def post(self):
        data = UserResgister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully"}, 201
