
from playhouse.db_url import connect
import os
db = connect(os.environ.get('DATABASE'))