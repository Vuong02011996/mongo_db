from mongoengine import Document


class BaseDAL:
    def __init__(self, model_class: Document):
        self.model_class = model_class
        collection_name = self.model_class._meta["collection"]
        self.collection = self.model_class._get_db()[collection_name]

    def save_document(self, list_data: list):
        # https://stackoverflow.com/questions/48028493/how-to-do-a-bulk-insert-with-mongoengine
        insert_list = [self.model_class(**data) for data in list_data]

        # bulk insert to MongoDB
        self.model_class.objects.insert(insert_list)

    def update_document(self, list_id: list, fields: dict):
        for mongo_id in list_id:
            self.model_class.objects(id=mongo_id).update(**fields)

    def delete_document(self, list_id: list):
        for mongo_id in list_id:
            self.model_class.objects(id=mongo_id).delete()

    # Function for query Using normal(find) or aggregation
    # https://docs.mongoengine.org/guide/querying.html#querying-the-database

    def find_all(self):
        return list(self.model_class.objects)

    def find_by_condition_field(self, field_condition: dict):
        # https://stackoverflow.com/questions/11876518/how-to-perform-such-filter-queries-in-mongoengine-on-nested-dicts-or-arrays-cont
        # https://docs.mongoengine.org/guide/querying.html#raw-queries
        return list(self.model_class.objects(__raw__=field_condition))

    # Aggregation
    def aggregate(self, pipeline):
        return self.model_class.objects.aggregate(pipeline)


