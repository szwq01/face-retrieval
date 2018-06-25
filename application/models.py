from peewee import *
from playhouse.postgres_ext import *

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
    detail = TextField()
    is_available = BooleanField(default=True)
    libhash = CharField()
    count = IntegerField(default=0)

    def get_photo(self, filename):
        pass

    def get_photos(self):
        pass


# class Algorithm(BaseModel):
#     name = CharField()


# class Feature(BaseModel):
#     name = CharField()
#     algorithm = ForeignKeyField(Algorithm, backref='features')
#     parameters = JSONField()

class Distance(BaseModel):
    name = CharField(unique=True)
    detail = TextField()
    filehash = CharField()
    library = ForeignKeyField(Library, backref='distances')
    is_available = BooleanField()


class Retrieval(BaseModel):
    user = ForeignKeyField(User, backref='retrieves')
    remark = TextField()
    library = ForeignKeyField(Library, backref='retrieves')
    distance = ForeignKeyField(Distance, backref='retrieves')
    strategy = CharField()
    max_round = IntegerField(default=8)
    rounds = ArrayField(CharField)
    status = CharField()
    max_round_faces = IntegerField(default=16)

    def get_next_round(self, selected):
        if len(self.rounds) >= self.max_round:
            return []


def create_tables():
    with db:
        db.create_tables([User, Library, Distance, Retrieval])
