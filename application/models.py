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


class Library(BaseModel):
    name = CharField(unique=True)
    detail = TextField(default='')
    is_available = BooleanField(default=True)
    hash = CharField(null=True)
    count = IntegerField(default=0)

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
    is_available = BooleanField(default=True)


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

class Iteration(BaseModel):
    retrieval = ForeignKeyField(Retrieval, backref='iterations')
    no = IntegerField()
    states = BinaryJSONField(null=True)
    results = ArrayField(CharField,default=lambda :[])
    selected = CharField(null=True)
    class Meta:
        primary_key = CompositeKey('retrieval', 'no')


def create_tables():
    with db:
        db.create_tables([User, Library, Distance, Retrieval,Iteration])
