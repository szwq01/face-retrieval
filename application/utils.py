
from playhouse.db_url import connect
import os
from . import const
db = connect(os.environ.get('DATABASE'))


def get_feature_path(library_name, feature_name):
    return os.path.join(const.LIBRARY_PATH, library_name, 'features',feature_name)

def get_photo_path(library_name, photo_name):
    return os.path.join(const.LIBRARY_PATH, library_name, 'photos',photoname)

def get_distance_path(library_name,distance_name):
    return os.path.join(const.LIBRARY_PATH, library_name, 'distances',distance_name)