design a  data model for ride sharing app , 


-- 
Consider the following 
Ask questions about data volume , make assumptions about what kind of platform are you considering (Redshift , teradata etc -0 this makes ome difference in certain approaches )
Mention the following , but they don't very much change your approach , it is important for the interviewer 
Data Model - Business entities , Business questions to answer 
        - Who and how the data will be accessed
        - How often the data will be loaded 
        - Performance consideration  (indexing , partitions , history tables (based on data volume ))
        - Security considerations (views , what kind of data should be stored , what should be excluded etc - don't go deep here )
        - Mention you will look at improvement ideas later 


-- While creating data model 
    - First list the tables
        - talk through while you are listing the tables 
        - Don't list columns yet 
        - Remember to add a date dimension table , location dimension ets , these are some standard tables in most DW
    - List columns , talk about your assumptions 
        - you are not expected to provide data type, but ask interviewer about it 
        - make assumption about teh cardinality , unique or not etc 
        - try to list in the order of importance , like IDs , surrogate keys etc come first 
        - Add surrogate keys where it make sense , opt for natural keys as much as you can , mention the trade off 
        - Talk about primary key foreign key etc 
        - mention if you are making any consideration for performance 
        


Business questions 

All metrics based on ride end timestamp 
1. Top 10 drivers in the last week , this is based on who has most number of completed rides in the last 7 days , and all rides need to have at least a 3 star rating 
2. A business analyst want to get all drivers who have had three consecutive bad ratings on previous day. (Consider only one day of data based on ride end timestamp, a bad rating is when the ride has a rating less than or equal to 3 star)
3. Find the top 5 drivers who has the most tip as a percentage of the ride cost (excluding tip) provided the driver has earned a minimum of $1000  for every month , for the last 6 months 
Expected out put here 
2022 jan driver01
2022 jan driver02
...............
2022  jan driver05
2022 feb driver01
........
2022 june driver01


Approach
    -For all questions , ask clarifying questions 
    - When possible try multiple approaches 
    - if there is a tricky way of doing it , try that first , mention alternative approaches (example , limit , sort etc )
    - Never abandon a question , start , if its too complicated , at least create partial answers 
        - for example in the 3rd question above , start with where clause , where you are eliminating dat older than six months 
        - now you aggregate the ride cost , and tip , use window function to partition data on each driver 
        - if possible try to do percentage as one step 
        - when not possible try CTE
