Learning how to use JSON in PostgreSQL involves understanding both the JSON data type and the functions and operators that PostgreSQL provides for working with JSON data. Here’s a step-by-step guide to get you started:

### 1. Understand JSON Basics
Before diving into PostgreSQL’s JSON capabilities, make sure you have a solid understanding of JSON itself:
- **JSON (JavaScript Object Notation)** is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
- It consists of key-value pairs, arrays, and nested structures.

### 2. Setup PostgreSQL
Make sure you have PostgreSQL installed. You can download it from the [official site](https://www.postgresql.org/download/) and follow the installation instructions for your operating system.

### 3. Create a Database and Table
Create a database and a table to practice storing JSON data:

```sql
CREATE DATABASE json_example;
\c json_example

CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    data JSON
);
```

### 4. Insert JSON Data
Insert JSON data into the table:

```sql
INSERT INTO people (data) VALUES ('{"name": "John", "age": 30, "city": "New York"}');
INSERT INTO people (data) VALUES ('{"name": "Jane", "age": 25, "city": "San Francisco"}');
```

### 5. Query JSON Data
Learn how to query JSON data using PostgreSQL’s JSON functions and operators.

#### 5.1. Retrieve JSON Data
Retrieve the JSON data:

```sql
SELECT data FROM people;
```

#### 5.2. Access JSON Fields
Use the `->` operator to get JSON objects and the `->>` operator to get JSON values as text:

```sql
SELECT data->'name' AS name FROM people;
SELECT data->>'name' AS name FROM people;
```

#### 5.3. Filter Based on JSON Data
Filter rows based on JSON values:

```sql
SELECT * FROM people WHERE data->>'city' = 'New York';
```

### 6. JSON Functions
PostgreSQL offers a variety of functions to work with JSON data:

#### 6.1. JSONB
For more efficient storage and querying, consider using `JSONB` instead of `JSON`. The difference is that `JSONB` stores JSON data in a binary format, which is more efficient for certain operations.

Create a table using `JSONB`:

```sql
CREATE TABLE people_b (
    id SERIAL PRIMARY KEY,
    data JSONB
);

INSERT INTO people_b (data) VALUES ('{"name": "John", "age": 30, "city": "New York"}');
INSERT INTO people_b (data) VALUES ('{"name": "Jane", "age": 25, "city": "San Francisco"}');
```

#### 6.2. Extract JSON Data
Extract elements and perform operations on JSONB:

```sql
SELECT data->'name' FROM people_b;
SELECT data->>'age'::int + 5 AS age_plus_five FROM people_b;
```

#### 6.3. JSONB Functions and Operators
- `jsonb_each`: Expands the outermost JSON object into a set of key-value pairs.
- `jsonb_array_elements`: Expands a JSON array to a set of JSON values.
- `jsonb_set`: Set new values in a JSONB document.

Example usage:

```sql
SELECT * FROM jsonb_each('{"name": "John", "age": 30, "city": "New York"}'::jsonb);

SELECT jsonb_set('{"name": "John", "age": 30, "city": "New York"}'::jsonb, '{age}', '35'::jsonb);
```

### 7. Indexing JSON Data
Create indexes to improve performance on JSONB columns:

```sql
CREATE INDEX idx_people_data ON people_b USING GIN (data);
```

### 8. Practice and Explore
- Work with nested JSON structures.
- Explore more advanced JSON functions like `jsonb_build_object`, `jsonb_pretty`, and `jsonb_strip_nulls`.

### Resources
- [PostgreSQL Documentation on JSON Types](https://www.postgresql.org/docs/current/datatype-json.html)
- [PostgreSQL JSON Functions and Operators](https://www.postgresql.org/docs/current/functions-json.html)

### Example Exercises
1. Create a table with a JSONB column and insert some data.
2. Write queries to extract specific fields from JSONB data.
3. Update JSONB data using JSONB functions.
4. Create indexes on JSONB columns and observe the performance improvements.

By following these steps and practicing with real data, you'll be able to effectively use JSON in PostgreSQL.