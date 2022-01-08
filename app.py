# -*- coding: utf-8 -*-
#!flask/bin/python
from re import template
from flask import Flask, jsonify, Blueprint, render_template
from flask import request
from flask_restplus import Api, Resource, fields, reqparse, inputs
from flask_cors import CORS
from datetime import datetime
from common import Base
from transfer import Transfer
import os
import sys
app = Flask(__name__)
api = Api(app, version='1.0', title='DataProvider API',
          description='KPI資料提供'
          )
# app.register_blueprint(blueprint)
CORS(app, supports_credentials=True, cors_allowed_origins='*')


transferNs = api.namespace('transfer', description='transfer')
transferML = api.model('transfer', {
    'source': fields.String(required=True, description='來源幣別', default='TWD', example='TWD'),
    'target': fields.String(required=True, description='目標幣別', default="TWD", example="TWD"),
    'amount': fields.Integer(required=True, description='⾦額數字', default=1, example=1),
})


@transferNs.route('', methods=['POST'])
@transferNs.response(200, 'Sucess')
@transferNs.response(201, 'Created Sucess')
@transferNs.response(204, 'No Content')
@transferNs.response(400, 'Bad Request')
@transferNs.response(401, 'Unauthorized')
@transferNs.response(403, 'Forbidden')
@transferNs.response(404, 'Not Found')
@transferNs.response(405, 'Method Not Allowed')
@transferNs.response(409, 'Conflict')
@transferNs.response(500, 'Internal Server Error')
class transfer(Resource):
    @transferNs.doc('取得參數')
    @transferNs.expect(transferML)
    def post(self):
        if not request:
            abort(400)
        elif not request.json:
            return {'Result': 'NG', 'Reason': 'Input is Empty or Type is not JSON'}, 400, Base.getheader()
        jsonData = request.json
        if "source" not in jsonData or "target" not in jsonData or "amount" not in jsonData:
            return {'Result': 'NG', 'Reason': 'Miss Parameter'}, 400, Base.getheader()
        elif not isinstance(jsonData['source'], str) or not isinstance(jsonData['target'], str) or not isinstance(jsonData['amount'], int):
            return {'Result': 'NG', 'Reason': 'Parameter Type Error'}, 400, Base.getheader()

        template = Base.transferTemplate()["currencies"]
        if jsonData['source'] not in template or jsonData['target'] not in template[jsonData['source']]:
            return {'Result': 'NG', 'Reason': 'Source or Target not in Template'}, 400, Base.getheader()
        return Transfer().transferSouceToTarget(jsonData['source'], jsonData['target'], jsonData['amount'])


def init_api():
    app.run(threaded=True, use_reloader=False, host='0.0.0.0',
            port=5000, debug=False)


if __name__ == '__main__':
    init_api()
