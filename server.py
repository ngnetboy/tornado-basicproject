from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from supereng import urlmap
from supereng.settings import config
import log_config

settings = dict(
    xsrf_cookies = config['xsrf_cookies'],
    login_url = config['login_url'],
    debug = config['debug'],
    cookie_secret = config['cookie_secret'],
)


def runserver():
    app = Application(
        handlers = urlmap.urlpattern,
        **settings
    )

    log_config.init(config['port'], config['log_console'], config['log_file'],
        config['log_file_path'], config['log_level'])

    httpserver = HTTPServer(app, xheaders=True)
    httpserver.listen(config['port'])

    IOLoop.current().start()


if __name__ == "__main__":
    runserver()
