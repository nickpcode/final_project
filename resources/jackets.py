import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required, current_user

# first argument is blueprints name
# second argument is it's import_name
# The third argument is the url_prefix so we don't have
# to prefix all our apis with /api/v1
jacket = Blueprint('jackets', 'jacket')

# used from flask react hmwk
@shirt.route('/', methods=["GET"])
def show_all_shirts():
    try:
        shirts = [model_to_dict(shirt) for shirt in models.Shirt.select()]
        print(shirts)
        return jsonify(data=shirts, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@shirt.route('/', methods=["POST"])
def create_shirts():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_shirt = models.Shirt.create(**payload)
    shirt_dict = model_to_dict(new_shirt)
    return jsonify(data=shirt_dict, status={"code": 201, "message": "Success"})

#individual show route
@shirt.route('/<id>', methods=["GET"])
def get_one_shirt(id):
    shirt = models.Shirt.get_by_id(id)
    print(shirt.__dict__)
    return jsonify(data=model_to_dict(shirt), status={"code": 200, "message": "Success"})

#update route
@shirt.route('/<id>', methods=["PUT"])
def change_shirt(id):
    payload = request.get_json()
    query = models.Shirt.update(**payload).where(models.Shirt.id == id)
    query.execute()
    return jsonify(data=model_to_dict(models.Shirt.get_by_id(id)), status={"code":200, "message": "Success"})

#delete route
@shirt.route('/<id>', methods=["DELETE"])
def donate_shirt(id):
    query = models.Shirt.delete().where(models.Shirt.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})