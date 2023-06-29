class UserModel:
    users = []

    @staticmethod
    def user_exists(username):
        return any(user['username'] == username for user in UserModel.users)

    @staticmethod
    def register_user(username, password):
        UserModel.users.append({'username': username, 'password': password})

    @staticmethod
    def authenticate_user(username, password):
        for user in UserModel.users:
            if user['username'] == username and user['password'] == password:
                return True
        return False
