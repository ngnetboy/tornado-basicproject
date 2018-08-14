import tornado.web
import tornado.ioloop
import tornado.httpserver

from tornado.options import define, options

from url import handlers
import config

define("port", type=int, default=8000, help="run server port")

async def init_db_pool():
    return await asyncpg.create_pool(database=config.sql_options['database'], host=config.sql_options['host'], 
        port=config.sql_options['port'], password=config.sql_options['password'], user=config.sql_options['user'])

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.redis = redis.StrictRedis(
            host=config.redis_options['host'],
            port=config.redis_options['port']
        )

def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            urls, **config.settings
        )
    app.pool = loop.run_until_complete(init_db_pool())

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()