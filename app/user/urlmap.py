from .handler import LoginHandler

urlpattern = (
    (r'/login/?', LoginHandler),
)