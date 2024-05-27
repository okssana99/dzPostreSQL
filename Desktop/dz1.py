print (':)')
#postgres=# CREATE DATABASE movies;
#CREATE DATABASE
#postgres=# \c movies;
#Ви тепер п?д'єднан? до бази даних "movies" як користувач "postgres".
#movies=# CREATE TABLE actors (
#movies(# id SERIAL PRIMARY KEY,
#movies(# name VARCHAR(100),
#movies(# nationality VARCHAR(50)
#movies(# );
#CREATE TABLE
#movies=# CREATE TABLE directors (
#movies(# id SERIAL PRIMARY KEY,
#movies(# name VARCHAR(100),
#movies(# nationality VARCHAR(50)
#movies(# );
#CREATE TABLE
#movies=# CREATE TABLE movies (
#movies(# id SERIAL PRIMARY KEY,
#movies(# title VARCHAR(200),
#movies(# release_date DATE,
#movies(# director_id INT REFERENCES directors(id)
#movies(# );
#CREATE TABLE
#movies=# INSERT INTO actors (name, birthdate) VALUES
#movies-# ('Tom Hanks', '1956-07-09'),
#movies-# ('Meryl Streep', '1949-06-22');
#ERROR:  column "birthdate" of relation "actors" does not exist
#РЯДОК 1: INSERT INTO actors (name, birthdate) VALUES
#                                   ^
#movies=# \d actors
#                                       ╥рсышЎ  "public.actors"
#  ╤ЄютяхЎ№   |          ╥шя           | ╤юЁЄєтрээ  | ╬сэєы ║Є№ё  |          ╟р чрьютўєтрээ ь
#-------------+------------------------+------------+-------------+------------------------------------
# id          | integer                |            | not null    | nextval('actors_id_seq'::regclass)
# name        | character varying(100) |            |             |
# nationality | character varying(50)  |            |             |
#▓эфхъёш:
#    "actors_pkey" PRIMARY KEY, btree (id)


#movies=# ALTER TABLE actors ADD COLUMN birthdate DATE;
#ALTER TABLE
#movies=# INSERT INTO actors (name, birthdate) VALUES
#movies-#     ('Tom Hanks', '1956-07-09'),
#movies-#     ('Meryl Streep', '1949-06-22');
#INSERT 0 2
#movies=# INSERT INTO directors (name, nationality) VALUES
#movies-#     ('Steven Spielberg', 'American'),
#movies-#     ('Quentin Tarantino', 'American');
#INSERT 0 2
#movies=# INSERT INTO movies (title, release_date, director_id) VALUES
#movies-#     ('Saving Private Ryan', '1998-07-24', 1),
#movies-#     ('Pulp Fiction', '1994-10-14', 2);
#INSERT 0 2
#movies=# SELECT * FROM actors FETCH FIRST 5 ROWS ONLY;
# id |     name     | nationality | birthdate
#----+--------------+-------------+------------
#  1 | Tom Hanks    |             | 1956-07-09
#  2 | Meryl Streep |             | 1949-06-22
#(2 Ё фъш)


#ovies=# TRUNCATE TABLE actors;
#TRUNCATE TABLE
#movies=#