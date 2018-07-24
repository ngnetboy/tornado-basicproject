from supereng.handler import BaseHandler
import logging

logger = logging.getLogger(__name__)



class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.warning("access login")
        self.write_json("hello login")