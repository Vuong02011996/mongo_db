from Aggregation.mongo_dal.base_dal import BaseDAL
from Aggregation.mongo_models.university import University


class UniversityDAL(BaseDAL):
    def __init__(self):
        super().__init__(University)

    # Define some function not yet in BaseDAL