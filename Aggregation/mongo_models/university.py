from mongoengine import (
    Document,
    LongField,
    IntField,
    DateTimeField,
    LazyReferenceField,
    StringField,
    ListField,
    EmbeddedDocument,
    FloatField,
    EmbeddedDocumentField,
    BooleanField,
)
import datetime


class Location(EmbeddedDocument):
    types = StringField()
    coordinates = ListField(FloatField(required=True), default=[])


class Student(EmbeddedDocument):
    year = IntField()
    number = IntField()


class University(Document):
    country = StringField()
    city = StringField()
    name = StringField()
    location = EmbeddedDocumentField(Location)
    students = ListField(EmbeddedDocumentField(Student))
