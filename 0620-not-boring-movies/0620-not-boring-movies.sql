# Write your MySQL query statement below

select * 
from 
cinema 
where description!='boring'
group by id
having mod(id,2)!=0
order by rating desc