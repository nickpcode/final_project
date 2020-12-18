import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required, current_user

# first argument is blueprints name
# second argument is it's import_name
# The third argument is the url_prefix so we don't have
# to prefix all our apis with /api/v1
shoe = Blueprint('shoes', 'shoe')

# used from flask react hmwk
@shoe.route('/', methods=["GET"])
def show_all_shoes():
    try:
        shoes = [model_to_dict(shoe) for shoe in models.Shoe.select()]
        print(shoes)
        return jsonify(data=shoes, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@shoe.route('/', methods=["POST"])
def create_shoes():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_shoe = models.Shoe.create(**payload)
    shoe_dict = model_to_dict(new_shoe)
    return jsonify(data=shoe_dict, status={"code": 201, "message": "Success"})

#individual show route
@shoe.route('/<id>', methods=["GET"])
def get_one_shoe(id):
    shoe = models.Shoe.get_by_id(id)
    print(shoe.__dict__)
    return jsonify(data=model_to_dict(shoe), status={"code": 200, "message": "Success"})

#update route
@shoe.route('/<id>', methods=["PUT"])
def change_shoe(id):
    payload = request.get_json()
    query = models.Shoe.update(**payload).where(models.Shoe.id == id)
    query.execute()
    return jsonify(data=model_to_dict(models.Shoe.get_by_id(id)), status={"code":200, "message": "Success"})

#delete route
@shoe.route('/<id>', methods=["DELETE"])
def donate_shoe(id):
    query = models.Shoe.delete().where(models.Shoe.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})