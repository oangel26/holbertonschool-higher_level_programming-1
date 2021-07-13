-- group city and average temp
SELECT city, AVG(value) average
FROM temperatures
GROUP BY city
ORDER BY average DESC
