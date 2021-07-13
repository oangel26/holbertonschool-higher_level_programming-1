-- max temp value in states
SELECT state, MAX(value) max_temp
FROM temperatures
GROUP BY state
ORDER BY MAX(value) DESC
