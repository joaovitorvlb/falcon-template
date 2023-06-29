import falcon
import json

class UserResource:
    def on_post(self, req, res):
        
        data = json.loads(req.bounded_stream.read().decode('utf-8'))

        print(data)
        # Aqui você pode adicionar a lógica para cadastrar o usuário
        # O corpo da requisição contém os dados do usuário
        # Exemplo: {'username': 'usuário', 'password': 'senha'}
        # Implemente a lógica de validação e persistência do usuário no banco de dados
        
        # Após cadastrar o usuário, você pode retornar uma resposta
        res.status = falcon.HTTP_201  # Created
        res.text = json.dumps({'message': 'Usuário cadastrado com sucesso'})

class LoginResource:
    def on_post(self, req, res):

        data = json.loads(req.bounded_stream.read().decode('utf-8'))

        print(data)
        # Aqui você pode adicionar a lógica para fazer o login do usuário
        # O corpo da requisição contém os dados de login
        # Exemplo: {'username': 'usuário', 'password': 'senha'}
        # Implemente a lógica de validação do usuário e autenticação
        
        # Após autenticar o usuário, você pode retornar uma resposta
        res.status = falcon.HTTP_200  # OK
        res.text = json.dumps({'message': 'Login bem-sucedido'})

class HomeResource:
    def on_get(self, req, res):

        data = json.loads(req.bounded_stream.read().decode('utf-8'))

        print(data)
        # Aqui você pode adicionar a lógica para retornar os dados da home
        # Implemente a lógica de consulta e formatação dos dados que serão retornados
        
        # Após obter os dados, você pode retornar uma resposta
        res.status = falcon.HTTP_200  # OK
        res.text = json.dumps({'data': data})

# Cria a instância da aplicação Falcon
app = falcon.App()

# Cria as rotas
app.add_route('/cadastro', UserResource())
app.add_route('/login', LoginResource())
app.add_route('/home', HomeResource())

# Executa a aplicação
if __name__ == '__main__':
    from wsgiref import simple_server

    httpd = simple_server.make_server('localhost', 8080, app)
    httpd.serve_forever()
