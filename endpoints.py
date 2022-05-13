from flask_restx import Namespace, fields, Resource
# 新增一個叫 account 的名稱空間
api = Namespace("account", description="帳號管理")


# ---------- 輸入輸出的格式 ----------
base_output_payload = api.model('基本輸出', {
    'status': fields.String(required=True, default=0),
    'message': fields.String(required=True, default="")
})

account_register_input_payload = api.model('註冊帳號input', {
    'email': fields.String(required=True, example="test01@gmail.com"),
    'password': fields.String(required=True, example="test")
})

account_register_output_payload = api.clone('註冊帳號output', base_output_payload)


# ---------- 路由以及功能 ----------
@api.route('', methods=['POST'])
@api.response(200, 'Sucess')
@api.response(201, 'Created Sucess')
@api.response(204, 'No Content')
@api.response(400, 'Bad Request')
@api.response(401, 'Unauthorized')
@api.response(403, 'Forbidden')
@api.response(404, 'Not Found')
@api.response(405, 'Method Not Allowed')
@api.response(409, 'Conflict')
@api.response(500, 'Internal Server Error')
class register(Resource):
    @api.expect(account_register_input_payload)
    @api.marshal_with(account_register_output_payload)
    def post(self):
        data = api.payload
        try:
            data = str({'email': data['email'], 'password': data['password']})
        except Exception:
            message = {'status': 1, 'message': 'error'}
        else:
            message = {'status': 0, 'message': ''}
        finally:
            return message