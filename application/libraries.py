import falcon
import json
from .models import Library


class Collection(object):

    def on_get(self, req, resp):
        libraries = Library.select()
        doc = [
            {
                'id': library.id,
                'name': library.name
            } for library in libraries
        ]
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200


class Item(object):

    def on_get(self, req, resp, id):
        library = Library.get_or_none(id=id)
        doc = {
            'id': library.id,
            'name': library.name
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200
