import falcon
import json
from models.user import UserModel

class UserController:
    def on_post(self, req, res):
        # Obter os dados do corpo da requisição
        data = json.loads(req.bounded_stream.read().decode('utf-8'))

        # Validar os dados do usuário
        if 'username' not in data or 'password' not in data:
            res.status = falcon.HTTP_400  # Bad Request
            res.text = json.dumps({'message': 'Nome de usuário e senha são obrigatórios'})
            return

        # Verificar se o usuário já está cadastrado
        username = data['username']
        if UserModel.user_exists(username):
            res.status = falcon.HTTP_409  # Conflict
            res.text = json.dumps({'message': 'Usuário já cadastrado'})
            return

        # Cadastrar o usuário
        UserModel.register_user(username, data['password'])

        # Responder com sucesso
        res.status = falcon.HTTP_201  # Created
        res.text = json.dumps({'message': 'Usuário cadastrado com sucesso'})
