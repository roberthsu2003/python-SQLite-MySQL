SELECT country_id
FROM country
WHERE country = 'United States';


SELECT city
FROM city
WHERE country_id = 103
ORDER BY city;

SELECT city
FROM city
WHERE country_id = (
	SELECT country_id
	FROM country
	WHERE country = 'United States')
ORDER BY city;


SELECT film_id
FROM film_category INNER JOIN  category USING(category_id)
WHERE name='Action';

SELECT film_id, title
FROM film
WHERE film_id IN(
	SELECT film_id
	FROM film_category INNER JOIN  category USING(category_id)
	WHERE name='Action')
ORDER BY film_id;
