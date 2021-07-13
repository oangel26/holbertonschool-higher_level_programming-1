-- group city and average temp
-- between july and august
SELECT city, AVG(value) avg_temp
FROM temperatures
WHERE month BETWEEN 7 and 8
GROUP BY city
ORDER BY AVG(value) DESC
LIMIT 3
