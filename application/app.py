import io
import json
import mimetypes
import os
import re
import uuid

import falcon
import falcon_jsonify

from . import const, iterations, libraries, photos, retrieves,distances
from .models import Distance, Library, User, create_tables
from .utils import db,get_distance_path,get_photo_path


def refresh_libs():
    lib_dir = const.LIBRARY_PATH
    libs = os.listdir(lib_dir)
    for lib_name in libs:
        library, created = Library.get_or_create(name=lib_name)
        photos = os.listdir(os.path.join(lib_dir, lib_name, 'photos'))
        library.count = len(photos)
        library.photos = photos
        library.save()
        distances = os.listdir(os.path.join(lib_dir, lib_name, 'distances'))
        for distance_name in distances:
            distance, created = Distance.get_or_create(
                name=distance_name, library=library)
            fp = get_distance_path(lib_name,distance_name)
            with open(fp,'r') as f:
                photos_list = f.readline().split()
            photos_map = {}
            for(index,value) in enumerate(photos_list):
                photos_map[value] = index
            distance.photos_map = photos_map
            distance.save()


def init_system():
    admin, created = User.get_or_create(username='admin',password='')


create_tables()
refresh_libs()
init_system()


class PeeweeConnectionMiddleware(object):
    def process_request(self, req, resp):
        db.connect(reuse_if_open=True)
        pass

    def process_response(self, req, resp, resource):
        if not db.is_closed():
            db.close()
        pass


api = application = falcon.API(middleware=[
    # PeeweeConnectionMiddleware(),
    falcon_jsonify.Middleware(help_messages=True),
    # ... other middlewares ...
])


class ImageStore(object):

    _CHUNK_SIZE_BYTES = 4096
    _IMAGE_NAME_PATTERN = re.compile(
        '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.[a-z]{2,4}$'
    )

    def __init__(self, storage_path, uuidgen=uuid.uuid4, fopen=io.open):
        self._storage_path = storage_path
        self._uuidgen = uuidgen
        self._fopen = fopen

    def save(self, image_stream, image_content_type):
        ext = mimetypes.guess_extension(image_content_type)
        name = '{uuid}{ext}'.format(uuid=self._uuidgen(), ext=ext)
        image_path = os.path.join(self._storage_path, name)

        with self._fopen(image_path, 'wb') as image_file:
            while True:
                chunk = image_stream.read(self._CHUNK_SIZE_BYTES)
                if not chunk:
                    break

                image_file.write(chunk)

        return name

    def open(self, library, name):
        # Always validate untrusted input!
        # if not self._IMAGE_NAME_PATTERN.match(name):
        #     raise IOError('File not found')

        image_path = os.path.join(self._storage_path, library, 'photos', name)
        stream = self._fopen(image_path, 'rb')
        stream_len = os.path.getsize(image_path)

        return stream, stream_len


image_store = ImageStore(const.LIBRARY_PATH)
api.add_route('/libraries', libraries.Collection())
api.add_route('/libraries/{name}', libraries.Item())
api.add_route('/distances', distances.Collection())
api.add_route('/distances/{id}', distances.Item())
api.add_route('/photos/{library}', photos.Collection())
api.add_route('/photos/{library}/{name}', photos.Item(image_store))
api.add_route('/retrieves', retrieves.Collection())
api.add_route('/retrieves/{retrieval_id}', retrieves.Item())
api.add_route('/retrieves/{retrieval_id}/iterations', iterations.Collection())
api.add_route('/retrieves/{retrieval_id}/iterations/{no}', iterations.Item())
