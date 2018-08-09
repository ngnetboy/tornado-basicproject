from tornado.web import RequestHandler
import json
from supereng.settings import config


class BaseHandler(RequestHandler):
    
    def write_json(self, data):
        result = {'error':0, 'errormsg':"success", 'data':None}
        result['data'] = data
        self.write(json.dumps(result))
        self.flush(include_footers=True)

    def write_message(self, message):
        data = {'error':0, 'errormsg':"success", 'data':None}
        if message != 'success':
            data['error'] = 1
            data['errormsg'] = message
        self.write(json.dumps(data))
        self.flush(include_footers=True)

    def write_error(self, status_code, **kwargs):
        title = kwargs.get("title", "")
        content = kwargs.get("content", "")
        if not config['debug']:
            if status_code == 403:
                self.write("403 aaaa</br>")
                #self.render("403.html")
            elif status_code == 404 or status_code == 405:
                self.write("404/405 bbbb</br>")
                #self.render("404.html")
            elif status_code == 500:
                self.write("500 cccc </br>")
                #self.render("500.html")
            self.write("Title: %s </br>" % title)
            self.write("Content: %s </br>" % content)
