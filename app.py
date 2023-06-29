import falcon
from controllers.home_controller import HomeController
from controllers.login_controller import LoginController
from controllers.user_controller import UserController

# Cria a instância da aplicação Falcon
app = falcon.App()

# Cria as rotas
app.add_route('/user', UserController())
app.add_route('/login', LoginController())
app.add_route('/home', HomeController())

# Executa a aplicação
if __name__ == '__main__':
    from waitress import serve

    serve(app, host='localhost', port=8000)
