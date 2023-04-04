CREATE TABLE my_table
  (column1 data_type1,
   column2 data_type2,
   ...
   )
LOCATION 's3://my-bucket/path/to/data/';
-- 
CREATE EXTERNAL TABLE my_table
  (column1 data_type1,
   column2 data_type2,
   ...
   )
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LOCATION 's3://my-bucket/path/to/data/';

----

CREATE TABLE my_table
WITH (
  format='TEXTFILE',
  external_location='s3://my-bucket/path/to/data/'
) AS 
SELECT column1, column2, ...
FROM my_source_table;
