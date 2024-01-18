-- Create a temp Table
CREATE TEMPORARY TABLE fan_from_country AS
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin;

-- Rank the countries with more fans
SELECT origin, nb_fans
FROM fan_from_country
ORDER BY nb_fans DESC;