USE courses_db; 

--- Generate 1000 users 
INSERT INTO users (email, first_name, last_name, password_hash, user_role,
    created_at, updated_at) SELECT 
    CONCAT('user', ROW_NUMBER() OVER (ORDER BY 1), '@example.com'), 
    CONCAT('First', ROW_NUMBER() OVER (ORDER BY 1)), 
    CONCAT('Last', ROW_NUMBER() OVER (ORDER BY 1)), 
    'password', 
    CASE WHEN ROW_NUMBER() OVER (ORDER BY 1) <= 900 THEN 'student' 
    ELSE 'administrator' END, 
    CURDATE(), 
    CURDATE() 
FROM information_schema.columns; 

--- Generate 1000 courses 
INSERT INTO courses (title, description, duration, start_date, end_date, instructor, 
created_at, updated_at ) SELECT 
    CONCAT('Course', ROW_NUMBER() OVER (ORDER BY 1)), 
    CONCAT('Description', ROW_NUMBER() OVER (ORDER BY 1)), 
    FLOOR(1 + RAND() * 1000), 
    CURDATE(), 
    CURDATE() 
FROM information_schema.columns; 

-- Generate 1000 instructors 
INSERT INTO instructors (instructor_id)
SELECT id 
FROM users 
WHERE user_role = 'administrator' 
LIMIT 1000; 

-- Generate 1000 modules 
INSERT INTO modules (title, duration, start_date, end_date, materials_id) 
SELECT 
    CONCAT('Module', ROW_NUMBER() OVER (ORDER BY 1)), 
    FLOOR(1 + RAND() * 10), 
    DATE_ADD(CURDATE(), INTERVAL FLOOR(1 + RAND() * 365) DAY), 
    DATE_ADD(CURDATE(), INTERVAL FLOOR(366 + RAND() * 365) DAY), 
    FLOOR(1 + RAND() * 1000) 
FROM information_schema.columns; 

--- Generate 1000 assignments 
INSERT INTO assignments (title, description, course_id, due_date, total_points, created_at, 
updated_at) 
SELECT 
    CONCAT('Assignment', ROW_NUMBER() OVER (ORDER BY 1)), 
    CONCAT('Description', ROW_NUMBER() OVER (ORDER BY 1)), 
    FLOOR(1 + RAND() * 100), 
    CURDATE(), 
    CURDATE() 
FROM information_schema.columns; 


--- Generate 1000 students 
INSERT INTO students (user_id) 
SELECT id 
FROM users 
WHERE user_role = 'student' 
LIMIT 1000; 

-- Geenrate 1000 students_courses 
INSERT INTO student_courses (student_id, course_id) 
SELECT 
    FLOOR(1 + RAND() * 1000), 
    FLOOR(1 + RAND() * 1000) 
FROM information_schema.columns
LIMIT 1000; 

--- Generate 1000 enrolmnets 
INSERT INTO enrollments (course_id, student_id, enrollment_data_path) 
SELECT 
    FLOOR(1 + RAND() * 1000), 
    FLOOR(1 + RAND() * 1000), 
    CONCAT('Path', ROW_NUMBER() OVER (ORDER BY 1)) 
FROM information_schema.columns 
LIMIT 1000; 

--- Generate 1000 materials 
INSERT INTO materials (course_id, description, file_path, url, created_at, updated_at) 
SELECT 
    FLOOR(1 + RAND() * 1000), 
    CONCAT('Material', ROW_NUMBER() OVER (ORDER BY 1)), 
    CONCAT('Description', ROW_NUMBER() OVER (ORDER BY 1)), 
    CONCAT('Filepath', ROW_NUMBER() OVER (ORDER BY 1)), 
    CONCAT('URL', ROW_NUMBER() OVER (ORDER BY 1)), 
    CURDATE(), 
    CURDATE() 
FROM information_schema.columns 
LIMIT 1000;