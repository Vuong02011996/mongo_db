# Concept:
    + $match() stage – filters those documents we need to work with
    + $group() stage – does the aggregation job
    + $sort()  stage – sorts the resulting documents the way we require (ascending or descending)

+ This way, we can break down a complex query into easier stages, in each of which we complete a different operation on the data.
+ The output of each stage will be the input of the next.
+ There is no limit to the number of stages used in the query, or how we combine them.

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
    1. $match
    2. $project
    3. $group
    4. 
# REF

+ https://studio3t.com/knowledge-base/articles/mongodb-aggregation-framework/
+ https://www.youtube.com/watch?v=IqBXKRrgy38&t=250s