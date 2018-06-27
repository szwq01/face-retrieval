import falcon
import json
from .models import Retrieval, Iteration
from .algorithms import get_next_iteration_random


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

    def on_post(self, req, resp, retrieval_id):
        no = req.get_json('no')
        select = req.get_json('select')
        retrieval = Retrieval.get_by_id(retrieval_id)
        if no >= retrieval.max_iteration:
            return
        if no == 0:
            states = {
                photo: {} for photo in retrieval.photos
            }
        else:
            last_iteration = Iteration.get(retrieval=retrieval, no=no-1)
            states = last_iteration.states
        iteration, created = Iteration.get_or_create(
            retrieval=retrieval, no=no, states=states)
        if retrieval.strategy == 'random':
            result = get_next_iteration_random(
                no, select, states, retrieval.max_iteration_faces)
            resp.json = result


class Item(object):

    def on_get(self, req, resp, id):
        retrieve = Retrieval.get_or_none(id=id)
        doc = {
            'id': retrieve.id,
            'user': retrieve.user,
            'status': retrieve.status,
            'rounds': retrieve.rounds
        }
        resp.body = json.dumps(doc, ensure_ascii=False)
        resp.status = falcon.HTTP_200

    def on_patch(self, req, resp, id):
        pass

    def on_delete(self, req, resp, id):
        pass
