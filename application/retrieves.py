import falcon
import json
from .models import Retrieval, Library, Distance, User
from . import utils

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
        max_iteration_faces = req.get_json('maxIterationFaces')
        max_iteration = req.get_json('maxIteration')
        strategy = req.get_json('strategy')
        photos = library.photos
        retrieve = Retrieval.create(
            user=user, library=library,strategy=strategy,distance=distance, photos=photos,max_iteration_faces=max_iteration_faces)
        # retrieve.save()
        resp.json = {'id': retrieve.id}


class Item(object):

    def on_get(self, req, resp, retrieval_id):
        retrieve = Retrieval.get_or_none(id=retrieval_id)
        # doc = {
        #     'id': retrieve.id,
        #     'userID': retrieve.user.id,
        #     'status': retrieve.status,
        #     'iterations': [iteration.to_json() for iteration in retrieve.iterations]
        # }
        doc = retrieve.to_json()
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_delete(self, req, resp, retrieval_id):
        pass
