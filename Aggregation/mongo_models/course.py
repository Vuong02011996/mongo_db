from mongoengine import (
    Document,
    StringField,
)
import datetime


class Course(Document):
    university = StringField()
    name = StringField()
    level = StringField()