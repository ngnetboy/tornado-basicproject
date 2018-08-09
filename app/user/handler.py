# coding=utf-8
from supereng.handler import BaseHandler
import logging

logger = logging.getLogger(__name__)



class LoginHandler(BaseHandler):

    def get(self, *args, **kwargs):
        logger.warning("access login")
        error_data = {
            "title":"error title 测试",
            "content":"error content"
        }
        self.send_error(500, **error_data)
        self.write_json("hello login")
