#coding:utf-8

from tornado.web import RequestHandler

class BaseHandler(RequestHandler):
    '''handler 基类'''
    def initialize(self):
        pass

    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def on_finish(self):
        pass

