import falcon
import json
from .models import Retrieval, Library, Distance, User


class Collection(object):

    def on_get(self, req, resp):
        retrieves = Retrieval.select()
        doc = [{
            'id': retrieve.id,
            'user': retrieve.user,
            'status': retrieve.status
        } for retrieve in retrieves]

        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        library = Library.get_by_id(req.get_json('libraryID'))
        user = User.get_by_id(1)
        distance = Distance.get_by_id(req.get_json('distanceID'))
        photos = library.get_photos()
        retrieve = Retrieval.create(
            user=user, library=library, distance=distance, photos=photos)
        # retrieve.save()
        resp.json = {'id': retrieve.id}


class Item(object):

    def on_get(self, req, resp, retrieval_id):
        retrieve = Retrieval.get_or_none(id=retrieval_id)
        doc = {
            'id': retrieve.id,
            'user': retrieve.user,
            'status': retrieve.status,
            'iterations': retrieve.iterations
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, retrieval_id):
        pass
