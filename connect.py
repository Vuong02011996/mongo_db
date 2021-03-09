from mongoengine import connect
# connect('project1')
from mongoengine import *
import datetime

class Page(Document):
    title = StringField(max_length=200, required=True)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)


connect('project1', host='localhost', port=27017, username='vuong', password='02011996', authentication_source='admin')
