from api.controllers.alliance_controller import alliance_route
from api.controllers.device_controller import device_route
from api.controllers.game_controller import game_route
from api.controllers.message_controller import message_route
from api.controllers.payments_controller import payments_route
from api.controllers.social_controller import social_route

controllers = [
    {
        "rule": "/game",
        "view_func": game_route
    },
    {
        "rule": "/social",
        "view_func": social_route
    },
    {
        "rule": "/",
        "view_func": device_route
    },
    {
        "rule": "/sms",
        "view_func": message_route
    },
    {
        "rule": "/alliance",
        "view_func": alliance_route
    },
    {
        "rule": "/payments",
        "view_func": payments_route
    }
]
