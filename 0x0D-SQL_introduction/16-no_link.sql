-- select all in second table
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC
