SELECT query_name,
       ROUND(AVG(rating * 100 / POSITION)) / 100 AS quality,
       ROUND(SUM(rating < 3) * 100 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
where query_name is not null
GROUP BY query_name
-- ORDER BY NULL;