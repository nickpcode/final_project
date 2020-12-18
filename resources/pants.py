import models

from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
# from flask_login import login_required, current_user

# first argument is blueprints name
# second argument is it's import_name
# The third argument is the url_prefix so we don't have
# to prefix all our apis with /api/v1
pant = Blueprint('pants', 'pant')

# used from flask react hmwk
@pant.route('/', methods=["GET"])
def show_all_pants():
    try:
        pants = [model_to_dict(pant) for pant in models.Pant.select()]
        print(pants)
        return jsonify(data=pants, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@pant.route('/', methods=["POST"])
def create_pants():
    payload = request.get_json()
    print(type(payload), 'payload')
    new_pant = models.Pant.create(**payload)
    pant_dict = model_to_dict(new_pant)
    return jsonify(data=pant_dict, status={"code": 201, "message": "Success"})

#individual show route
@pant.route('/<id>', methods=["GET"])
def get_one_pant(id):
    pant = models.Pant.get_by_id(id)
    print(pant.__dict__)
    return jsonify(data=model_to_dict(pant), status={"code": 200, "message": "Success"})

#update route
@pant.route('/<id>', methods=["PUT"])
def change_pant(id):
    payload = request.get_json()
    query = models.Pant.update(**payload).where(models.Pant.id == id)
    query.execute()
    return jsonify(data=model_to_dict(models.Pant.get_by_id(id)), status={"code":200, "message": "Success"})

#delete route
@pant.route('/<id>', methods=["DELETE"])
def donate_pant(id):
    query = models.Pant.delete().where(models.Pant.id==id)
    query.execute()
    return jsonify(data="resource successfully deleted", status={"code": 200, "message": "resource successfully deleted"})