from tornado.web import RequestHandler
import json


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
        if not config['debug']:
            if status_code == 403:
                self.write_json("403 error")
                #self.render("403.html")
            elif status_code == 404 or 405:
                self.write_json("404/405 error")
                #self.render("404.html")
            elif status_code == 500:
                self.write_json("500 error")
                #self.render("500.html")