DROP DATABASE IF EXISTS courses_db;

CREATE DATABASE courses_db;

USE courses_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(30) UNIQUE NOT NULL,
    first_name VARCHAR(30),
    last_name VARCHAR(20),
    password_hash VARCHAR(30),
    user_role ENUM('student', 'administrator'),
    created_at DATE,
    updated_at DATE
);

CREATE TABLE courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(30) UNIQUE NOT NULL,
    description VARCHAR(30),
    duration INT,
    start_date DATE,
    end_date DATE,
    instructor INT,
    created_at DATE,
    updated_at DATE,
    CONSTRAINT fk_instructor FOREIGN KEY (instructor) REFERENCES instructors(id)
);

CREATE TABLE instructors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    instructor_id INT NOT NULL,
    CONSTRAINT fk_instructor_id FOREIGN KEY (instructor_id) REFERENCES users(id)
);

CREATE TABLE modules (
    module_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(30) NOT NULL,
    duration INT,
    start_date DATE,
    end_date DATE,
    materials_id INT,
    CONSTRAINT fk_materials FOREIGN KEY (materials_id) REFERENCES materials(id)
);

CREATE TABLE assignments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(30),
    description VARCHAR(255),
    course_id INT,
    due_date DATE,
    total_points DOUBLE,
    created_at DATE,
    updated_at DATE,
    CONSTRAINT fk_course_id FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE students_courses (
    id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES students(id),
    CONSTRAINT fk_course_id FOREIGN KEY (course_id) REFERENCES courses(id)
);

CREATE TABLE enrollments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    course_id INT,
    student_id INT,
    enrollment_data_path VARCHAR(200), 
    CONSTRAINT fk_course_id FOREIGN KEY (course_id) REFERENCES courses(id), 
    CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES students(id)
);

CREATE TABLE materials(
    id INT PRIMARY KEY AUTO_INCREMENT, 
    course_id INT, 
    title VARCHAR(30), 
    description TEXT, 
    file_path VARCHAR(200), 
    url VARCHAR(200), 
    created_at DATE, 
    updated_at DATE
); 

