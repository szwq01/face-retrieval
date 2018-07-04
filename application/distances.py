import falcon
import json
from .models import Distance


class Collection(object):

    def on_get(self, req, resp):
        lib_id = req.get_param('libraryID', None)
        if lib_id is not None:
            distances = Distance.select().where(Distance.library == lib_id)
        else:
            distances = Distance.select()
        doc = [
            {
                'id': distance.id,
                'name': distance.name
            } for distance in distances
        ]
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200


class Item(object):

    def on_get(self, req, resp, id):
        distance = Distance.get_or_none(id=id)
        doc = {
            'id': distance.id,
            'name': distance.name
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
