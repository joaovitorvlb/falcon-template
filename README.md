# Começando uma api com python e Falcom

A instenção é criar uma aplicação web que apartir da index seja retornado um bem-vindo em json.

## Instalação do virtiualenv

* sudo apt install -y python3-venv


## Criação do virtual env

* virtualenv myenv

## Ativando o ambiente virtual criado

* source myenv/bin/activate

## Quando precisar pode desativar o ambiente virtual

* deactivate

## Inatalação da ferramentas Falcon

* pip install falcon

## Execução da aplicação, ececutando o app.py

* python app.py

Acesse http://localhost:8080 em seu navegador para interagir com a aplicação.

Neste exemplo, temos as seguintes rotas:

    Rota inicial: '/home' - Exibe uma mensagem de boas-vindas.
    Rota de cadastro de usuário: '/cadastro' - Exibe um formulário de cadastro de usuário. Quando o formulário é enviado via método POST, o usuário é cadastrado e a mensagem de sucesso é exibida.
    Rota de login: '/login' - Exibe um formulário de login. Quando o formulário é enviado via método POST, verifica-se se o usuário e senha correspondem aos dados cadastrados. Se forem corretos, uma mensagem de boas-vindas é exibida; caso contrário, uma mensagem de erro é exibida.

Primeiro se acessa a tela de cadastro via GET e usuário via POST e enviado e fica salva na seção.


Para testar começaremos a trestar as rotas no postman:


    Cadastro de Usuário:
        Método: POST
        URL: http://localhost:8080/cadastro
        Cabeçalhos:
            Content-Type: application/x-www-form-urlencoded
        Corpo (form data):
            username: [nome_de_usuario]
            password: [senha]

    Login de Usuário:
        Método: POST
        URL: http://localhost:8080/login
        Cabeçalhos:
            Content-Type: application/x-www-form-urlencoded
        Corpo (form data):
            username: [nome_de_usuario]
            password: [senha]
        Resposta: Você receberá um token JWT como resposta no corpo da mensagem.

    Acesso à Rota Home:
        Método: GET
        URL: http://localhost:8080/home

