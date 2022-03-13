# Write your MySQL query statement below

select request_at as "Day"
, cast(cancelled/total_ as decimal(5,2))  as "Cancellation Rate"
from (
 select request_at 
 , count(T.id) total_ 
 , sum(case  when status = 'completed' then 0 else 1 end) cancelled
 from trips t 
 join 
    (select users_id as id from  Users where banned = 'NO' and role = 'client') u 
 on t.client_id = u.id
 join (select users_id  as id from  Users where banned = 'NO' and role = 'driver') d
 on d.id = t.driver_id
where request_at between '2013-10-01' and '2013-10-03'
 group by request_at
    )X