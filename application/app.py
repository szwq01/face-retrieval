import falcon
from .utils import db
from .photos import Photos
from .retrieves import Retrieves
# from peewee import *
from .models import create_tables


def init_photos():
    pass


def init_features():
    pass


def init_distances():
    pass


def init_system():
    pass


class PeeweeConnectionMiddleware(object):
    def process_request(self, req, resp):
        db.connect()

    def process_response(self, req, resp, resource):
        if not db.is_closed():
            db.close()


api = application = falcon.API(middleware=[
    PeeweeConnectionMiddleware(),
    # ... other middlewares ...
])

photos = Photos()
retrieves = Retrieves()
api.add_route('/photos', photos)
api.add_route('/retrieves', photos)
