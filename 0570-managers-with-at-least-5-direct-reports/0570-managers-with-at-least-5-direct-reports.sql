-- select e.name from employee e
select e.name from employee e
inner join
(select e1.managerid from employee e1 group by managerid having count(e1.managerid)>=5) as s
on
s.managerid = e.id 

-- select e.name
-- from (select e1.managerid from employee e1 group by managerid having count(e1.managerid)) as s


-- select e.name from employee e
-- join
-- employee e1
-- on 
-- e.id = e1.id
-- group by e1.managerid
-- having count(e1.managerid)>=5

