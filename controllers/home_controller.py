import falcon
import json
from views.home_view import HomeView

class HomeController:
    def on_get(self, req, res):
        # Obter os dados da home
        home_data = HomeView.get_home_data()

        # Responder com sucesso
        res.status = falcon.HTTP_200  # OK
        res.text = json.dumps(home_data)
