# Write your MySQL query statement below


select distinct(teacher_id) , count(distinct(subject_id)) as cnt
from 
teacher
Group by teacher_id






