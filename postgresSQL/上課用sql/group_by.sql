SELECT customer_id
FROM payment
GROUP BY customer_id
ORDER BY customer_id ASC;

SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
ORDER By customer_id;


SELECT customer_id, SUM(amount) as 總合
FROM payment
GROUP BY customer_id
ORDER By 總合 DESC;


SELECT 
	first_name || ' ' || last_name as full_name,
	SUM(amount) as 總合
FROM payment INNER JOIN customer ON payment.customer_id = customer.customer_id 
GROUP BY full_name
ORDER BY 總合 DESC;


SELECT staff_id, COUNT(payment_id)
FROM payment
GROUP BY staff_id


SELECT staff_id,customer_id,SUM(amount)
FROM payment
GROUP BY staff_id,customer_id
ORDER BY staff_id
