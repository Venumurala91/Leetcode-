# Write your MySQL query statement below
-- select v.customer_id , count(customer_id) as Count_no_trans
-- select v.customer_id , count(customer_id) as Count_no_trans

select v.customer_id ,count(v.customer_id) as count_no_trans
from 
visits v
left join
transactions t
on 
v.visit_id = t.visit_id
where t.transaction_id is null
Group by v.customer_id