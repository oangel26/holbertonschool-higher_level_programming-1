-- group by score
SELECT score, COUNT(score) average
FROM second_table
GROUP BY score
