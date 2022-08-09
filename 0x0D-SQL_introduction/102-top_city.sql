-- Displays top 3 city's temperatures during July and August
SELECT city,
    AVG(value) avg_temp
FROM temperatures
WHERE month = 7
    OR month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
