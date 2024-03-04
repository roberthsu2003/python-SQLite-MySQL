DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS contacts;

CREATE TABLE customers(
	customer_id INT GENERATED ALWAYS AS IDENTITY,
	customer_name VARCHAR(255) NOT NULL,
	PRIMARY KEY(customer_id)
);



CREATE TABLE contacts(
	contact_id INT GENERATED ALWAYS AS IDENTITY,
	customer_id INT,
	contact_name VARCHAR(255) NOT NULL,
	phone VARCHAR(15),
	email VARCHAR(100),
	PRIMARY KEY(contact_id),
	CONSTRAINT fk_customer FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers(customer_name)
VALUES('BlueBird Inc'),
      ('Dolphin LLC');	   
	   
INSERT INTO contacts(customer_id, contact_name, phone, email)
VALUES(1,'John Doe','(408)-111-1234','john.doe@bluebird.dev'),
      (1,'Jane Doe','(408)-111-1235','jane.doe@bluebird.dev'),
      (2,'David Wright','(408)-222-1234','david.wright@dolphin.dev');
	  
/*沒有設定ON DELETE和ON UPDATE*/
/*DEFAULT NO ACTION*/
/*下面所以違反限定,出現錯誤*/
DELETE FROM customers
WHERE customer_id = 1


