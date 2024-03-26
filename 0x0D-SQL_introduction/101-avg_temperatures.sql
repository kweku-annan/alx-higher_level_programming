-- Displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, AVG(value) AS average_temp
FROM temperatures
GROUP BY city
ORDER BY average_temp
