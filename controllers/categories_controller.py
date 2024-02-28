from flask import jsonify, Request

from db import db
from models.categories import Categories, categories_schema, category_schema
from util.reflection import populate_object


def category_add(req: Request):
    post_data = req.form if req.form else req.json
    fields = ['category_name']
    req_fields = ['category_name']
    values = {}

    for field in fields:
        field_data = post_data.get(field)
        values[field] = field_data
        if field in req_fields and not values[field]:
            return jsonify(f"{field} is required."), 400
        
    new_category = Categories.get_new_category()

    populate_object(new_category, post_data)

    db.session.add(new_category)
    db.session.commit()

    return jsonify(category_schema.dump(new_category)), 201


def categories_get_all(req: Request):
    categories_query = db.session.query(Categories).all()

    return jsonify(categories_schema.dump(categories_query)), 200


def category_get_by_id(category_id):
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    return jsonify(category_schema.dump(category_query)), 200


def category_update_by_id(req: Request, category_id):
    post_data = req.form if req.form else req.json
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    if category_query is None:

        return jsonify({"message": "category not found."}), 404
    
    if 'category_name' in post_data:

        category_query.category_name = post_data['category_name']

    db.session.commit()

    return jsonify({"message": "category updated successfully."})


def category_delete_by_id(req: Request, category_id):
    category_query = db.session.query(Categories).filter(Categories.category_id == category_id).first()

    try:

        db.session.delete(category_query)

        db.session.commit()

        return jsonify({"message": "Category deleted successfully"}), 200
    
    except:

        return jsonify({"message": "Category not found"}), 404