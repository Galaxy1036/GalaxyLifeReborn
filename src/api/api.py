from flask import Blueprint

from api.controllers import controllers


routes = Blueprint('api', __name__)

for controller in controllers:
    routes.add_url_rule(
                        controller['rule'],
                        view_func=controller['view_func'],
                        methods=['POST']
                        )
