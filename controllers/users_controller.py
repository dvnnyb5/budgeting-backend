from flask import jsonify, Request
from flask_bcrypt import generate_password_hash

from db import db
from models.users import Users, user_schema, users_schema
from util.reflection import populate_object
from lib.authenticate import authenticate


def user_add(req: Request):
    post_data = req.form if req.form else req.json
    fields = ['username', 'email', 'password']
    req_fields = ['username', 'email', 'password']
    values = {}

    for field in fields:
        field_data = post_data.get(field)
        values[field] = field_data
        if field in req_fields and not values[field]:
            return jsonify(f"{field} is required."), 400

    new_user = Users.get_new_user()

    populate_object(new_user, post_data)

    new_user.password = generate_password_hash(new_user.password).decode('utf8')

    db.session.add(new_user)
    db.session.commit()

    return jsonify(user_schema.dump(new_user)), 201

@authenticate
def users_get_all(req: Request):
    users_query = db.session.query(Users).all()

    return jsonify(users_schema.dump(users_query)), 200


def user_get_by_id(user_id):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    return jsonify(user_schema.dump(user_query)), 200


def user_update_by_id(req: Request, user_id):
    post_data = req.form if req.form else req.json
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    if user_query is None:

        return jsonify({"message": "User not found"}), 404
    
    if 'username' in post_data:

        user_query.username = post_data["username"]

    if 'email' in post_data:

        user_query.email = post_data["email"]

    if 'password' in post_data:

        user_query.password = post_data["password"]

    db.session.commit()

    return jsonify({"message": "User updated successfully."}), 200
    


def user_delete_by_id(req: Request, user_id):
    user_query = db.session.query(Users).filter(Users.user_id == user_id).first()

    try:

        db.session.delete(user_query)

        db.session.commit()

        return jsonify({"message": "User deleted successfully"}), 200
    
    except:

        return jsonify({"message": "User not found"}), 404