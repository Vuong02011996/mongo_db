from mongoengine import connect, Document, StringField, IntField

# connect(
#     db='db_name_1',
#     host='localhost',
#     port=11038,
#     username='root',
#     password='example',
#     alias="db1"
# )
connect(
    db='test_db',
    host='0.0.0.0',
    port=11038,
    username="root",
    password="example",
    authentication_source="admin"
)

# connect("db", host="mongodb://" + "abc" + ":" + "abc"  + "@localhost:" + str(11038) + '/?authSource=admin')


class Students(Document):
    student_id = StringField(required=True)
    name = StringField(max_length=50)
    age = IntField()

    def __init__(self, id, name, age):
        super().__init__()
        self.student_id = id
        self.name = name
        self.age = age


student1 = Students(id="123", name="Admin", age=20)
student1.save()
