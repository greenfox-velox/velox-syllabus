# Database

## Materials
- https://www.youtube.com/watch?v=FR4QIeZaPeM
- https://www.youtube.com/watch?v=NvrpuBAMddw
- https://www.youtube.com/watch?v=IIdfqFxercg
- https://www.youtube.com/watch?v=yPu6qV5byu4
- https://www.youtube.com/watch?v=h7mhFTAJvxA

## Assignment review
- data
- dbms
- database
    - navigational
    - relational
    - oodb
- SQL
- primary key
- normalizations
    - 1nf
    - 2nf
    - 3nf
- create database
- use database
- create table
    - text
    - varchar
    - integer
    - datetime
    - ...
- describe
- insert into
- value / values
- select
    - where
    - operators
        - =
        - >
        - <
        - <>
        - IN
        - ...
    - group by
    - having
    - sql functions
        - sum
        - max
        - min
        - avg
        - ...
- join
    - wtf :)

## Workshop

### Practice Exercises
- Complete all challenges here:
- http://sqlbolt.com/
- https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_movie_query_core/
- https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_movie_query_extra/
- https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_social_query_core/
- https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_social_query_extra/
- https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_movie_mod/
- https://lagunita.stanford.edu/courses/DB/SQL/SelfPaced/courseware/ch-sql/seq-exercise-sql_social_mod/

### MySQL
- Install MySQL for your computer
- (you can install MySQL Workbench as well)
- Create a new database on your computer:
```mysql
CREATE DATABASE bookstore;
```
- Import all data from `data.sql` file:
```
$ mysql bookstore < data.sql
```
- for windows users: Navigate to the directory where you have mysql and issue this command, changing the bold values to your file/database locations.
```
c:\mysql\bin\> mysql -u USERNAME -p bookstore < data.sql
```
- list all tables
- select all data from all tables
- create a query selecting all books with its name, authors name, category name, publishers name and price

---
- create a database for Todos
- plan and create the only table you'll need
- use auto incremented primary key
- add some sample data from sql
