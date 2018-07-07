from peewee import *
from playhouse.postgres_ext import *
from . import const
import os
from .utils import db

retrieval_strategies = {
    'random': None,
    'most_similar': None,
    'entropy': None
}


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    is_admin = BooleanField(default=False)
    def to_json(self):
        return {
            'userName': self.username,
            'isAdmin': self.is_admin
        }

class Library(BaseModel):
    name = CharField(unique=True)
    detail = TextField(default='')
    is_available = BooleanField(default=True)
    hash = CharField(null=True)
    photos = ArrayField(CharField,null=True)
    count = IntegerField(default=0)

    def to_json(self):
        return {
            'name':self.name,
            'detail':self.detail,
            'isAvailable': self.is_available,
            'hash':self.hash,
            'count':self.count
        }
    # def get_photo(self, filename):
    #     pass

    def get_photos(self):
        photos = os.listdir(os.path.join(const.LIBRARY_PATH, self.name, 'photos'))
        return sorted(photos)


# class Algorithm(BaseModel):
#     name = CharField()


# class Feature(BaseModel):
#     name = CharField()
#     algorithm = ForeignKeyField(Algorithm, backref='features')
#     parameters = JSONField()

class Distance(BaseModel):
    name = CharField(unique=True)
    detail = TextField(default='')
    hash = CharField(null=True)
    library = ForeignKeyField(Library, backref='distances')
    photos_map = JSONField(null=True)
    is_available = BooleanField(default=True)
    def to_json(self):
        return {
            'name': self.name,
            'detail': self.detail,
            'hash': self.hash,
            'libraryID': self.library.id
        }

class Retrieval(BaseModel):
    user = ForeignKeyField(User, backref='retrieves')
    remark = TextField(default='')
    library = ForeignKeyField(Library, backref='retrieves')
    distance = ForeignKeyField(Distance, backref='retrieves')
    strategy = CharField(default='random')
    max_iteration = IntegerField(default=8)
    status = CharField(default='pending')
    photos = ArrayField(CharField)
    max_iteration_faces = IntegerField(default=16)
    iterator_pointer = IntegerField(default=0)

    def get_next_round(self, selected):
        if len(self.rounds) >= self.max_round:
            return []

    def to_json(self):
        return {
            'user': self.user.to_json(),
            'remark': self.remark,
            'library': self.library.to_json(),
            'strategy': self.strategy,
            'maxIteration': self.max_iteration,
            'status': self.status,
            'maxIterationFaces': self.max_iteration_faces,
            'iteratorPointer': self.iterator_pointer,
            'iterations': [iteration.to_json() for iteration in self.iterations],
            'distance': self.distance.to_json()
        }

class Iteration(BaseModel):
    retrieval = ForeignKeyField(Retrieval, backref='iterations')
    no = IntegerField()
    states = BinaryJSONField(null=True)
    results = ArrayField(CharField,default=lambda :[])
    selected = CharField(null=True)
    class Meta:
        primary_key = CompositeKey('retrieval', 'no')
    def to_json(self):
        return {
            'retrievalID': self.retrieval.id,
            'no':self.no,
            'results': self.results,
            'selected': self.selected
        }

def create_tables():
    with db:
        db.create_tables([User, Library, Distance, Retrieval,Iteration])
