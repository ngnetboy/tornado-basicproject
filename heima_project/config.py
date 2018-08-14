# coding:utf-8
import os


#Application
settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
    "template_path" : os.path.join(os.path.dirname(__file__), "template"),
    #base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    "cookie_secret" : 'Aq6ZxqmtRaKC7KJcV3mKsNYXuRxrXEDakQfF5isGPY0=', 
    #"xsrf_cookies" : 'D1SWn/uIQlSo24yWo8eokszUht6oU0ZCjqh8Vgnrpbs=',
    "xsrf_cookies" : True,
    "debug" : True,
}

# postgresql
sql_options = dict(
    database='ihome', 
    host='127.0.0.1', 
    port=5432, 
    password='', 
    user='postgres'
)

#redis
redis_options = dict(
    host='127.0.0.1',
    port=6379
)