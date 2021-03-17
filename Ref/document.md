1. NoSQL và SQL
   
    
2. Primary key in MongDB.
   
    _id: trường định danh cho từng document.
   
    _id: có một giá trị ObjectID duy nhất.
   
3. Sort:
    Mode: 1 tăng dần (esc SQL), -1 giảm dần (desc SQL)
   
4. Aggregation
   
    + clusters out your data from multiple different documents
    + then used and operates in lots of ways (on these clustered data) to return a combined result 
    + The output of each stage will be the input of the next.
    + that of the count(*) along with the 'group by' used in SQL.
    + three different ways of performing aggregation
      
        + The aggregation pipeline.
        + The map-reduce function.
        + Single purpose aggregation methods.
    
    + Syntax:
        ```
            db.collection_name.aggregate(aggregate_operation)
        ```
    
    ref: https://www.w3schools.in/mongodb/aggregation/
   
   + Example:
    ```
    db.writers.aggregate([{$group : {_id : "$author", TotalBooksWritten : {$sum : 1}}}])
    ```
5. Map-reduce.

6. REF:

   https://studio3t.com/knowledge-base/articles/mongodb-aggregation-framework/

