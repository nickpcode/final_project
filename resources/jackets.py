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
@jacket.route('/', methods=["GET"])
def show_all_jackets():
    try:
        jackets = [model_to_dict(jacket) for jacket in models.Jacket.select()]
        print(jackets)
        return jsonify(data=jackets, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@jacket.route('/', methods=["POST"])
def create_jackets():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_jacket = models.Jacket.create(**payload)
    jacket_dict = model_to_dict(new_jacket)
    return jsonify(data=jacket_dict, status={"code": 201, "message": "Success"})

#individual show route
@jacket.route('/<id>', methods=["GET"])
def get_one_jacket(id):
    jacket = models.Jacket.get_by_id(id)
    print(jacket.__dict__)
    return jsonify(data=model_to_dict(jacket), status={"code": 200, "message": "Success"})

#update route
@jacket.route('/<id>', methods=["PUT"])
def change_jacket(id):
    payload = request.get_json()
    query = models.Jacket.update(**payload).where(models.Jacket.id == id)
    query.execute()
    return jsonify(data=model_to_dict(models.Jacket.get_by_id(id)), status={"code":200, "message": "Success"})

#delete route
@jacket.route('/<id>', methods=["DELETE"])
def donate_jacket(id):
    query = models.Jacket.delete().where(models.Jacket.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})