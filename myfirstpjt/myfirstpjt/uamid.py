#
import random
from myfirstpjt.settings import UAPOOL
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __init__(self,ua=''):
        self.ua=ua
    def process_request(self, request, spider):
        thisua=random.choice(UAPOOL)
        print("UA:"+thisua)
        request.headers.setdefault('User-Agent',thisua)