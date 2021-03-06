<div align ="center">
<img src="./src/spongebob-database.gif" />
</div>

### Basics:
After installation, 
- In windows or linux there is only one database called postgres
- In Mac there will be 2 users postgres and name of your username.

**Things to be noted before writing the SQL query :**
1. Weriting queries to retrive information
2. Designing the schema or structure of the database.
3. Understanding when to use advance features.
4. Managing the databae in a production environment.

### Database design :
1. Ehat kind of data we need to store.
2. What properties does this data should have
3. What type of data does each of those propeties contains?

Take **Cities table :**
|name  | country | Population | Area |
|------|---------|------------|------|
|String|   String|         Int| Float|

```
CREATE TABLE CITIES(
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(20),
    COUNTRY VARCHAR(20),
    POPULATION INT,
    AREA 
)
```
### Filtering the records with WHERE :

**ORDER in which the query get executes :**
```
# Executes third
SELECT NAME , AREA

# Executes 1st
FROM cities

#executes secons
WHERE area > 4000;
```

Along with where we can also use IN:
```
SELECT CITY,COUNTRY
FROM CITIES
WHERE CITY NOT IN ('chennai','Shangai');
```
We can compund with math operator with **AND, OR, NOT**.

**Using between :**

```
SELECT CITY, AREA
FROM CITIES
WHERE AREA BETWEEN 1000 AND 5000;
```


**Updating the rows**
```
UPDATE CITIES SET POPULATION = 400000
WHERE CITY ='Tokyo';
```

**Deleting the rows**

If we didn't mention WHERE then all the data will be deleted. 
```
UPDATE CITIES SET POPULATION = 400000
WHERE CITY ='Tokyo';
```
### To Describe the cities:

information_schema.columns have all the information about the columns about all the tables.
<table border="2px">
<tr>
    <td>Postgres</td>
    <td>MySQL</td>
</tr>
<tr>
<td>
    <code>
    SELECT 
    table_name, 
    column_name, 
    data_type 
    FROM 
    information_schema.columns
    WHERE 
   table_name = 'cities';
    </code>
</td>

<td>
    <code>
    DESC cities;
    </code>
</td>
<tr>
</table>

### Relationships:

There are 3 types of relationships:

1. one to one
2. one to many
3. many to many



**PGAdmin 4 :** 

This is a web based tool to manage and inspect postgres database. We can run querys and modify data in the database.

This is also used to connect to the remote database also. (like AWS, GCP)

Inside the postgres we can have multiple database, but if we are building a application there will be only one database in our system. The ground rule is one application one database.

**Data types :**

- Data types like SERIAL -> used to increment the data.
- Data type like VARCHAR -> used to tell which data to be stored in the table.

Types of data we can store:
1. Numbers
2. currency
3. Binary
4. Date/Time
5. Character
6. JSON
7. Geometric
8. Range
9. Arrays
10. Boolean
11. XML
12. UUID

**_Numbers can be :_**
1. Storing numbers without any decimal point

    - smallint, int, bigint
2. Storing numbers without any decimal point (With auto increment)
    
    - smallserial, serial, bigserial 
3. With decimal point
    
    - decimal, numeric, real, double precision, float. 

When we need to store a number with **Extream accuracy** then we have to use numeric.

Need to store a number which decimal does not make any sense use double precision.

**_Date, Time, Timestamp :_**

- We can give any formate of date: This will be converted to the date by postgres.
```
SELECT('NOV-9-1999'::DATE);
```
This will store the date like
| date     |
|----------|
|1999-11-09|

- We can store the date with timezone or time without timezone.
- **Whatever the time formate we are giving this will be converted to 24 hrs time**
- By default it is time without timezone.

```
SELECT('PM 01:23'::TIME);

SELECT('PM 01:23'::TIME WITHOUT TIME ZONE);

```
- With timzone converts the timezone to UTC; here we have to give WITH TIME ZONE explicitly.
```
SELECT(' 01:23 PM EST'::TIME WITH TIME ZONE);
```

|timetz        |
|--------------|
|13:23:00-05:00|

- For timestamp

```
SELECT('01 3 2000 1:20 PM PST'::TIMESTAMP);
```

### Side Validation and constrains:

**Row Level validations :**

- NOT NULL -> This will show error, when we make the column as the NULL.
- DEFAULT  -> This will give the default value when we insert a row in the table.
- UNIQUE   -> If we can't have two rows with same value.
- CHECK    -> To check the data is logically correct.

### Data structure design patterns:






### Baics:
|  Command            | What it do                  |
|---------------------|-----------------------------|
|  \l                 |  To list all the databases. |
| \c <database name>  |  To use a database.         |
| \dt                 | To show all the tables      |

### Permissions in postgres: 

**What is Schema?**
- Schema is a collection of logical structure of data. In Postgre, Schema is a named collection f tables, views, functions and constraints.



- When we say **create user** then we mean: Create role and login permission.

- The only difference between the user and the role is **user is able to login** where the **role can not login**.

- When we use the SQL statement to create the user in postgre:
```
CREATE USER testuser WITH PASSWORD 'secret_password';

```
- If we want to create the same user with the CREATE ROLE:
```
CREATE ROLE testuser WITH PASSWORD 'secret_password';
 
```
**_IMPORATANT TO NOTE:_**
- All the new users and roles are by default granted this public role, and can create object in public schema.

**Difference between public schema and public user :**

- When a new database is created postgre will create a schema named public.
- All the new users and roles by default can create an object in public schema.
- This is not good.


### Commands for Postgre commands.

|  Command | What it do                  |
|----------|-----------------------------|
|  \dp     |  To list all the privileges |

