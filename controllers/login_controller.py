import falcon
import json
from models.user import UserModel

class LoginController:
    def on_post(self, req, res):
        # Obter os dados do corpo da requisição
        data = json.loads(req.bounded_stream.read().decode('utf-8'))

        # Validar os dados do login
        if 'username' not in data or 'password' not in data:
            res.status = falcon.HTTP_400  # Bad Request
            res.text = json.dumps({'message': 'Nome de usuário e senha são obrigatórios'})
            return

        # Verificar se as credenciais são válidas
        username = data['username']
        password = data['password']
        if UserModel.authenticate_user(username, password):
            res.status = falcon.HTTP_200  # OK
            res.text = json.dumps({'message': 'Login bem-sucedido'})
        else:
            res.status = falcon.HTTP_401  # Unauthorized
            res.text = json.dumps({'message': 'Credenciais inválidas'})
