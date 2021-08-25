from mongoengine import connect
from Aggregation.mongo_dal.university_dal import UniversityDAL
from Aggregation.mongo_dal.course_dal import CourseDAL
from pprint import pprint

"""
from Aggregation.mongo_models.university import University
university = University()
I want to create many document university I must create many object university and assign value for each university
So, Using dal (data access level) to manage them.
"""
connect(
    db='test_db',
    host='0.0.0.0',
    port=11038,
    username="root",
    password="example",
    authentication_source="admin"
)
university_dal = UniversityDAL()
course_dal = CourseDAL()

universities = [{
    "country": 'Spain',
    "city": 'Salamanca',
    "name": 'USAL',
    "location": {
        "types": 'Point',
        "coordinates": [-5.6722512, 17, 40.9607792]
    },
    "students": [
        {"year": 2014, "number": 24774},
        {"year": 2015, "number": 23166},
        {"year": 2016, "number": 21913},
        {"year": 2017, "number": 21715}
    ]
},
    {
        "country": 'Spain',
        "city": 'Salamanca',
        "name": 'UPSA',
        "location": {
            "types": 'Point',
            "coordinates": [-5.6691191, 17, 40.9631732]
        },
        "students": [
            {"year": 2014, "number": 4788},
            {"year": 2015, "number": 4821},
            {"year": 2016, "number": 6550},
            {"year": 2017, "number": 6125}
        ]
    }
]

course = [
    {
        "university": 'USAL',
        "name": 'Computer Science',
        "level": 'Excellent'
    },
    {
        "university": 'USAL',
        "name": 'Electronics',
        "level": 'Intermediate'
    },
    {
        "university": 'USAL',
        "name": 'Communication',
        "level": 'Excellent'
    }
]


def find_all_document():
    data = list(university_dal.find_all())
    list_id = []
    for document in data:
        list_id.append(document.id)
    print(list_id)
    list_id = [list_id[0]]
    return list_id


def update_document(list_id):
    fields = {"country": 'Spain'}
    university_dal.update_document(list_id, fields)


def save_document():
    university_dal.save_document(universities)
    course_dal.save_document(course)


def aggregate_match():
    pipeline = [{"$match": {"country": 'Spain', "city": 'Salamanca'}}]
    data = list(university_dal.aggregate(pipeline))
    pprint(data)


def aggregate_project():
    pipeline_project = [
        {"$project": {"_id": 0, "country": 1, "city": 1, "name": 1}}
    ]
    data = list(university_dal.aggregate(pipeline_project))
    pprint(data)


def aggregate_group():
    pipeline_group = [
        {"$group": {"_id": '$country', "totaldocs": {"$sum": 1}}}
    ]
    data = list(university_dal.aggregate(pipeline_group))
    pprint(data)


def aggregate_out():
    pipeline_out = [
        {"$group": {"_id": '$name', "totaldocs": {"$sum": 1}}},
        {"$out": 'aggResults'}]
    data = list(university_dal.aggregate(pipeline_out))
    pprint(data)


def aggregate_unwind():
    pipeline_unwind = [
        {"$match": {"name": 'USAL'}},
        {"$unwind": {"path": "$students"}}
    ]
    data = list(university_dal.aggregate(pipeline_unwind))
    pprint(data)


def aggregate_sort():
    pipeline_sort = [
        {"$match": {"name": 'USAL'}},
        {"$unwind": "$students"},
        {"$project": {"_id": 0, 'students.year': 1, 'students.number': 1}},
        {"$sort": {'students.number': -1}}
    ]
    data = list(university_dal.aggregate(pipeline_sort))
    pprint(data)


def aggregate_limit():
    pipeline_limit = [
        {"$match": {"name": 'USAL'}},
        {"$unwind": "$students"},
        {"$project": {"_id": 0, 'students.year': 1, 'students.number': 1}},
        {"$sort": {'students.number': -1}},
        {"$limit": 2}
    ]
    data = list(university_dal.aggregate(pipeline_limit))
    pprint(data)


def aggregate_add_fields():
    pipeline_add_fields = [
        {"$match": {"name": 'USAL'}},
        {"$addFields": {"foundation_year": 1218}}
    ]
    data = list(university_dal.aggregate(pipeline_add_fields))
    pprint(data)


def aggregate_count():
    pipeline_count = [
        {"$unwind": '$students'},
        {"$count": 'total_documents'}
    ]
    data = list(university_dal.aggregate(pipeline_count))
    pprint(data)


def aggregate_lookup():
    pipeline_lookup = [
        {"$match": {"name": 'USAL'}},
        {"$project": {"_id": 0, "name": 1}},
        {
            "$lookup": {
                "from": 'course',
                "localField": 'name',
                "foreignField": 'university',
                "as": 'course'
            }
        }
    ]
    data = list(university_dal.aggregate(pipeline_lookup))
    pprint(data)


def aggregate_sort_by_count():
    pipeline_sort_by_count = [
        {"$sortByCount": '$level'}
    ]
    data = list(course_dal.aggregate(pipeline_sort_by_count))
    pprint(data)


if __name__ == '__main__':
    # aggregate_unwind()
    # aggregate_sort()
    # aggregate_limit()
    # aggregate_add_fields()
    # aggregate_count()
    # aggregate_lookup()
    aggregate_sort_by_count()

    # university_dal.delete_document(list_id)
