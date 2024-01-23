/*
problem statement :
Given a list of bus routes, find the shortest path from source to destination.
-- source and destination are not in the same route

*/
*/

create table destination_q
(source_ varchar(50),
destination_ varchar(50))
;

insert into destination_q values ('A','B');
insert into destination_q values ('B','A');
insert into destination_q values ('C','D');
insert into destination_q values ('D','C');
insert into destination_q values ('X','Y');
insert into destination_q values ('Y','Z');

commit;


select *
from destination_q


select LEAST(A.source_,A.destination_)
,coalesce(GREATEST(B.source_,B.destination_),GREATEST(A.source_,A.destination_))
from destination_q A
left join destination_q B
on A.source_ = B.destination_
and A.destination_ = B.Source_
group by 1,2



