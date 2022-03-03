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
