# Write your MySQL query statement below
select class
from 
courses c
Group by class
having count(student)>=5