from Aggregation.mongo_models.course import Course
from Aggregation.mongo_dal.base_dal import BaseDAL


class CourseDAL(BaseDAL):
    def __init__(self):
        super().__init__(Course)