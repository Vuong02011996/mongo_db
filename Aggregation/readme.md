# Introduce
When you start with MongoDB, you will use the *find()* command for querying data and it will probably be
sufficient, but as soon as you start doing anything more advanced than data retrieval, you will need to known
about MongoDB aggregation pipeline.
![](Aggregation%20Framework.png)

+ $match() stage – filters those documents we need to work with
+ $group() stage – does the aggregation job
+ $sort()  stage – sorts the resulting documents the way we require (ascending or descending)

## How to work
+ The input of the pipeline can be one or several collections.
+ The pipeline then performs successive transformations on the data until our goal is achieved.
+ This way, we can break down a complex query into easier stages, in each of which we complete a different operation on the data.
+ The output of each stage will be the input of the next.
+ There is no limit to the number of stages used in the query, or how we combine them.
+ To achieve optimum query performance there are a number of best practices to take into account.
# Syntax
    ```
    pipeline = [
      { $match : { … },
      { $group : { … },
      { $sort : { … },
      ...
    ]
    db.collectionName.aggregate(pipeline, options)
    ```
# Regarding aggregation stage limits
+ Up to 100 MB of RAM can be used per aggregation stage.
  + ```db.collectionName.aggregate(pipeline, { allowDiskUse : true })``` to using disk(slower)
+ The documents returned by the aggregation query, either as a cursor or stored via $out() in another collection, 
are limited to 16MB
# Concept:
  1. _**$match**_
     1. The $match stage allows us to choose just those **documents** from a collection that we want to work with
     2. Example
     ```python
      pipeline = [{"$match" : { "country" : 'Spain', "city" :'Salamanca' }}]
      data = list(university_dal.aggregate(pipeline))
      ```
     
  2. **_$project_**
     1. It is good practice to return only those **fields** you need.
     2. Example
     ```python
      pipeline = [
          {"$project": {"_id": 0, "country": 1, "city": 1, "name": 1}}
      ]
      data = list(university_dal.aggregate(pipeline))
      ```
  3. _**$group**_
     1. We can perform all the aggregation or summary queries that we need, such as finding counts, totals, averages or maximums
     2. Example
     ```python
     pipeline_group = [
      {"$group": {"_id": '$country', "totaldocs": {"$sum": 1}}}]
      ```

  4. _**$out**_
     1. It allows you to carry the results of your aggregation over into a new collection, or into an existing one after dropping it, or even adding them to the existing documents
     2. The $out() operator must be the last stage in the pipeline.
     3. Example:
     ```python
      pipeline_out = [
          {"$group": {"_id": '$name', "totaldocs": {"$sum": 1}}},
          {"$out": 'aggResults'}]
      ```
  5. **_$unwind_**
     1. You cannot work directly on the elements of an array within a document with stages such as $group(). The $unwind() stage enables us to work with the values of the fields within an array.
     2. Where there is an array field within the input documents, you will sometimes need to output the document several times, once for every element of that array.
     3. Each copy of the document has the array field replaced with the successive element.
     4. Example
     ```python
         pipeline_unwind = [
        {"$match": {"name": 'USAL'}},
        {"$unwind": {"path": "$students"}}
      ]
      pipeline_unwind = [
          {"$match": {"name": 'USAL'}},
          {"$unwind": {"path": "$location.coordinates"}}
      ]
      ```
  6. _**$sort**_
     1. You need the $sort() stage to sort your results by the value of a specific field.
     2. descending order (-1), increase order (1)
     3. Example:
     ```python
      pipeline_sort = [
              {"$match": {"name": 'USAL'}},
              {"$unwind": "$students"},
              {"$project": {"_id": 0, 'students.year': 1, 'students.number': 1}},
              {"$sort": {'students.number': -1}}
          ]
      ```
  
  7. _**$limit**_
     1. What if you are only interested in the first two results of your query
     2. Example:
     ```python
      pipeline_limit = [
          {"$match": {"name": 'USAL'}},
          {"$unwind": "$students"},
          {"$project": {"_id": 0, 'students.year': 1, 'students.number': 1}},
          {"$sort": {'students.number': -1}},
          {"$limit": 2}
      ]
      ```
     
  8. _**$addFields**_
     1. It is possible that you need to make some changes to your output in the way of new fields
     2. Example
     ```python
     pipeline_add_fields = [
             {"$match": {"name": 'USAL'}},
             {"$addFields": {"foundation_year": 1218}}
         ]
     ```
  
  9. **_$count_**
     1. The $count() stage provides an easy way to check the number of documents obtained in the output of the previous stages of the pipeline
     2. Example
     ```python
         pipeline_count = [
             {"$unwind": '$students'},
             {"$count": 'total_documents'}
         ]
     ```
  10. _**$lookup**_
      1. Using the $lookup(), here is an aggregate query that merges fields from two collections.
      2. Example:
      ```python
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
      ```
  
  11. _**$sortByCount**_
      1. This stage is a shortcut for grouping, counting and then sorting in descending order the number of different values in a field
      2. Example:
      ```python
         pipeline_sort_by_count = [
             {"$sortByCount": '$level'}
         ]
      ```

# REF

+ https://studio3t.com/knowledge-base/articles/mongodb-aggregation-framework/
+ https://docs.mongodb.com/manual/reference/operator/aggregation-pipeline/
+ https://www.youtube.com/watch?v=IqBXKRrgy38&t=250s