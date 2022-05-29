import os

from flask import Blueprint, jsonify, request

from project.api.models import Table
from project import db


tables_blueprint = Blueprint('tables', __name__)


@tables_blueprint.route('/tables', methods=['GET', 'POST'])
def all_tables():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    if request.method == 'POST':
        post_data = request.get_json()
        manufacturer = post_data.get('manufacturer')
        model = post_data.get('model')
        photo = post_data.get('photo')
        price = post_data.get('price')
        db.session.add(Table(manufacturer=manufacturer, model=model, photo=photo, price=price))
        db.session.commit()
        response_object['message'] = 'Table added!'
    else:
        response_object['tables'] = [table.to_json() for table in Table.query.all()]
    return jsonify(response_object)


@tables_blueprint.route('/tables/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@tables_blueprint.route('/tables/<table_id>', methods=['PUT', 'DELETE'])
def single_table(table_id):
    response_object = {
      'status': 'success',
      'container_id': os.uname()[1]
    }
    table = Table.query.filter_by(id=table_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        table.manufacturer = post_data.get('manufacturer')
        table.model = post_data.get('model')
        table.photo = post_data.get('photo')
        table.price = post_data.get('price')
        db.session.commit()
        response_object['message'] = 'Table updated!'
    if request.method == 'DELETE':
        db.session.delete(table)
        db.session.commit()
        response_object['message'] = 'Table removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
