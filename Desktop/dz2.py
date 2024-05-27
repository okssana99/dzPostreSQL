print (":)")
#"Частина 2" 
#\c movies
#Ви тепер п?д'єднан? до бази даних "movies" як користувач "postgres".
# CREATE TABLE Directors1 (
#movies(# director_id SERIAL PRIMARY KEY,
#movies(# name VARCHAR(255),
#movies(# birthdate DATE
#movies(# );
#CREATE TABLE
#movies=# INSERT INTO Directors1 (name, birthdate) VALUES
#movies-# ('Steven Spielberg', '1946-12-18'),
##movies-# ('Christopher Nolan', '1970-07-30'),
#movies-# ('Quentin Tarantino', '1963-03-27');
#INSERT 0 3
#movies=# CREATE TABLE Movies1 (
#movies(# movie_id SERIAL PRIMARY KEY,
#movies(# title VARCHAR(255),
#movies(# release_date DATE
#movies(# );
#CREATE TABLE
#movies=# INSERT INTO Movies1 (title, release_date) VALUES
#movies-# ('Forrest Gump', '1994-07-06'),
#movies-# ('The Dark Knight', '2008-07-18'),
#movies-# ('Pulp Fiction', '1994-05-12');
#INSERT 0 3
#movies=# CREATE TABLE Actors1 (
#movies(# actor_id SERIAL PRIMARY KEY,
#movies(#     name VARCHAR(255),
#movies(#     birthdate DATE,
#movies(#     gender_type VARCHAR(10)
#movies(# );
#CREATE TABLE
#movies=# INSERT INTO Actors1 (name, birthdate, gender_type) VALUES
#movies-# ('Tom Hanks', '1956-07-09', 'Male'),
#movies-# ('Meryl Streep', '1949-06-22', 'Female'),
#movies-# ('Leonardo DiCaprio', '1974-11-11', 'Male');
#INSERT 0 3
# CREATE TABLE Actor_Movie (
#movies(#     actor_id INT,
#movies(#     movie_id INT,
#movies(# FOREIGN KEY (actor_id) REFERENCES Actors1(actor_id),
#movies(# FOREIGN KEY (movie_id) REFERENCES Movies1(movie_id),
#movies(# PRIMARY KEY (actor_id, movie_id)
#movies(# );
#CREATE TABLE
#movies=# INSERT INTO Actor_Movie (actor_id, movie_id) VALUES
#movies-# (1, 1),
#movies-# (2, 1),
#movies-# (3, 2);
#INSERT 0 3
#movies=# CREATE TABLE Director_Movie (
#movies(#     director_id INT,
#movies(#     movie_id INT,
#movies(# FOREIGN KEY (director_id) REFERENCES Directors1(director_id),
#movies(# FOREIGN KEY (movie_id) REFERENCES Movies1(movie_id),
#movies(# PRIMARY KEY (director_id, movie_id)
#movies(# );
#CREATE TABLE
#movies=# INSERT INTO Director_Movie (director_id, movie_id) VALUES
#movies-# (1, 1),
#movies-# (2, 2),
#movies-# (3, 3);
#INSERT 0 3

#"Частина 3"
#postgres=# \c postgres
#Ви тепер п?д'єднан? до бази даних "postgres" як користувач "postgres".
#postgres=# CREATE TABLE departments (
#postgres(#     id SERIAL PRIMARY KEY,
#postgres(#     name VARCHAR(100) NOT NULL
#postgres(# );
#CREATE TABLE
#postgres=# CREATE TABLE teachers (
#postgres(#     id SERIAL PRIMARY KEY,
#postgres(#     first_name VARCHAR(50) NOT NULL,
#postgres(#     last_name VARCHAR(50) NOT NULL,
#postgres(#     department_id INT,
#postgres(#     FOREIGN KEY (department_id) REFERENCES departments(id)
#postgres(# );
#CREATE TABLE
#postgres=# CREATE TABLE groups (
#postgres(#     id SERIAL PRIMARY KEY,
#postgres(#     name VARCHAR(50) NOT NULL,
#postgres(#     department_id INT,
#postgres(#     FOREIGN KEY (department_id) REFERENCES departments(id)
#postgres(# );
#CREATE TABLE
#postgres=# CREATE TABLE students (
#postgres(#     id SERIAL PRIMARY KEY,
#postgres(#     first_name VARCHAR(50) NOT NULL,
#postgres(#     last_name VARCHAR(50) NOT NULL,
#postgres(#     group_id INT,
#postgres(#     FOREIGN KEY (group_id) REFERENCES groups(id)
#postgres(# );
#CREATE TABLE
#postgres=# INSERT INTO departments (name) VALUES
#postgres-# ('Computer Science'),
#postgres-# ('Mathematics'),
#postgres-# ('Physics');
#INSERT 0 3
#postgres=# INSERT INTO teachers (first_name, last_name, department_id) VALUES
#postgres-# ('John', 'Doe', 1),
#postgres-# ('Jane', 'Smith', 2),
#postgres-# ('Robert', 'Johnson', 3),
#postgres-# ('Emily', 'Williams', 1),
#postgres-# ('Michael', 'Brown', 2);
#INSERT 0 5
#postgres=# INSERT INTO groups (name, department_id) VALUES
#postgres-# ('CS50', 1),
#postgres-# ('Math101', 2),
#postgres-# ('Phys101', 3),
#INSERT 0 4
#postgres=# INSERT INTO students (first_name, last_name, group_id) VALUES
#postgres-# ('Alice', 'Johnson', 1),
#postgres-# ('Bob', 'Smith', 2),
#postgres-# ('Charlie', 'Williams', 3),
#postgres-# ('David', 'Brown', 1),
#postgres-# ('Eva', 'Davis', 2),
#postgres-# ('Frank', 'Miller', 3),
#postgres-# ('Grace', 'Jones', 4),
#postgres-# ('Henry', 'Anderson', 1),
#postgres-# ('Ivy', 'Moore', 2),
#postgres-# ('Jack', 'Taylor', 3),
#postgres-# ('Kate', 'White', 4),
#postgres-# ('Leo', 'Martin', 1),
#postgres-# ('Mia', 'Young', 2),
#postgres-# ('Noah', 'Lee', 3),
#postgres-# ('Olivia', 'Harris', 4),
#postgres-# ('Paul', 'Clark', 1),
#postgres-# ('Quinn', 'Evans', 2),
#postgres-# ('Ryan', 'Wright', 3),
#postgres-# ('Sophia', 'Walker', 4),
#postgres-# ('Tyler', 'Hill', 1);
#INSERT 0 20
#Запити:
#1.
#postgres=# SELECT students.first_name, students.last_name, groups.name AS group_name
#postgres-# FROM students
#postgres-# JOIN groups ON students.group_id = groups.id;
# first_name | last_name | group_name
#------------+-----------+------------
# Alice      | Johnson   | CS50
# Bob        | Smith     | Math101
# Charlie    | Williams  | Phys101
# David      | Brown     | CS50
# Eva        | Davis     | Math101
# Frank      | Miller    | Phys101
# Grace      | Jones     | CS101
# Henry      | Anderson  | CS50
# Ivy        | Moore     | Math101
# Jack       | Taylor    | Phys101
# Kate       | White     | CS101
# Leo        | Martin    | CS50
# Mia        | Young     | Math101
# Noah       | Lee       | Phys101
# Olivia     | Harris    | CS101
# Paul       | Clark     | CS50
# Quinn      | Evans     | Math101
# Ryan       | Wright    | Phys101
# Sophia     | Walker    | CS101
# Tyler      | Hill      | CS50
#(20 Ё фъ│т)

#2.
#postgres=# SELECT teachers.first_name, teachers.last_name, departments.name AS department_name
#postgres-# FROM teachers
#postgres-# JOIN departments ON teachers.department_id = departments.id;
# first_name | last_name | department_name
#------------+-----------+------------------
# John       | Doe       | Computer Science
# Jane       | Smith     | Mathematics
# Robert     | Johnson   | Physics
# Emily      | Williams  | Computer Science
# Michael    | Brown     | Mathematics
#(5 Ё фъ│т)

#3.
#postgres=# SELECT groups.name AS group_name, COUNT(students.id) AS student_count
#postgres-# FROM groups
#postgres-# LEFT JOIN students ON groups.id = students.group_id
#postgres-# GROUP BY groups.name;
# group_name | student_count
#------------+---------------
# Math101    |             5
# CS50       |             6
# CS101      |             4
# Phys101    |             5
#(4 Ё фъш)

#4.
#postgres=# SELECT departments.name AS department_name,
#postgres-#        teachers.first_name AS teacher_first_name,
#postgres-#        teachers.last_name AS teacher_last_name,
#postgres-#        groups.name AS group_name,
#postgres-#        students.first_name AS student_first_name,
#postgres-#        students.last_name AS student_last_name
#postgres-# FROM departments
#postgres-# JOIN teachers ON departments.id = teachers.department_id
#postgres-# JOIN groups ON departments.id = groups.department_id
#postgres-# JOIN students ON groups.id = students.group_id
#postgres-# WHERE teachers.last_name IN ('Smith', 'Williams', 'Johnson')
#postgres-# ORDER BY group_name, student_last_name;
# department_name  | teacher_first_name | teacher_last_name | group_name | student_first_name | student_last_name
#------------------+--------------------+-------------------+------------+--------------------+-------------------
# Computer Science | Emily              | Williams          | CS101      | Olivia             | Harris
# Computer Science | Emily              | Williams          | CS101      | Grace              | Jones
# Computer Science | Emily              | Williams          | CS101      | Sophia             | Walker
# Computer Science | Emily              | Williams          | CS101      | Kate               | White
# Computer Science | Emily              | Williams          | CS50       | Henry              | Anderson
# Computer Science | Emily              | Williams          | CS50       | David              | Brown
# Computer Science | Emily              | Williams          | CS50       | Paul               | Clark
# Computer Science | Emily              | Williams          | CS50       | Tyler              | Hill
# Computer Science | Emily              | Williams          | CS50       | Alice              | Johnson
# Computer Science | Emily              | Williams          | CS50       | Leo                | Martin
# Mathematics      | Jane               | Smith             | Math101    | Eva                | Davis
# Mathematics      | Jane               | Smith             | Math101    | Quinn              | Evans
# Mathematics      | Jane               | Smith             | Math101    | Ivy                | Moore
# Mathematics      | Jane               | Smith             | Math101    | Bob                | Smith # Physics          | Robert             | Johnson           | Phys101    | Noah               | Lee
# Physics          | Robert             | Johnson           | Phys101    | Frank              | Miller
# Physics          | Robert             | Johnson           | Phys101    | Jack               | Taylor
# Physics          | Robert             | Johnson           | Phys101    | Charlie            | Williams
# Physics          | Robert             | Johnson           | Phys101    | Ryan               | Wright
#(20 Ё фъ│т)
