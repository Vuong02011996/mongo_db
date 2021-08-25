from mongoengine import connect

connect(
    db='db_name_1',
    host='127.0.0.1',
    port=11038,
    username='root',
    password='example',
)
# Mongo engine also allows connection with multiple database.
# You need to provide unique alias name for each database.
connect(
    db='db_name_2',
    host='127.0.0.1',
    port=11038,
    username='root',
    password='example',
    alias="db1"
)
connect(
    db='db2',
    host='127.0.0.1',
    port=11038,
    username='root',
    password='example',
    alias="db2"
)