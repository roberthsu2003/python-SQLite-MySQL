SELECT first_name
FROM customer;

SELECT first_name, last_name, email
FROM customer;

SELECT *
FROM customer;

SELECT first_name || ' ' || last_name AS full_name,email 
FROM customer;

SELECT NOW()