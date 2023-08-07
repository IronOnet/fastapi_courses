# Course Management System 

This is a course managment system built with python 
The aim of a course managment system is to simplify the process of delivering 
educational courses, promotes online learning, and enhances the learning experiences 
for both instructors and students by providing a centralized platform for course 
administration, content delivery, communication, assessment, and progress tracking.

## Funcitonal Requirements 

- Course creation and Organization: allow administrators to create 
    and structure courses. They can define course materials, syllabi, 
    learning objectives, assessment, and other relevant content 

- Provide tools for managing and organizing course content including, uploading 
    documents, videos presentations, and other multi-media resources. It allows 
    instructors to create and organize lessons, modules or units within a course 

- Course delivery: enables online course delivery allowing learners to access course 
    material and participate in activities remotely. It may include features like 
    discussion forums, chat rooms, and live

- Enrollement and registration: Students can enroll in courses through the CMS 
    it manages the registration procedss, including user authentication, user roles 
    and access control to ensure that only authorized users can access the courses 

- Communication and collaboration: CMS provides communication tools for instructors 
    and students to interact and collaborate. This may include messaging systems, email notifications, announcements, and discussion boards for fostering student engagment and facilitating instructor-student communication 

- Assignment and assessment managment: CMS allows instructors to create and distribute assignments to students. 

- Progress tracking and reporting: CMS tracks and records student progress, 
    including completed activities, grades and overall course performance. 
    instructors and administrators can generate reports to analyze student 
    performance, identify areas for improvment, and evalutate the effectiveness of
    the courses.

- Administration and analytics: CMS offers administrative features, allowing 
    administrators to manage user accounts, roles and permissions. It may also 
    provide analytics and reporting capabilities for administrators to monitor system
    usage, track course enrollments, and collect data for evaluation and decision-making process 

## Data Model 

    - Course: 
        - course_id 
        - course_title 
        - course_description 
        - course_duration 
        - start_date: 
        - end_date 
        - course_instructor

    - Modules/Lessons: 
        - module_id 
        - module_title 
        - module_duration 
        - module_materials 
        - course_id

    - Assignment/Assessment: 
        - assignment_id 
        - assignment_title: 
        - assignment_description 
        - due_date: date 
        - total_points: 

    - Student: 
        - user_id
        - enrolement_date 
    
    - student_course: 
        - course_id 
        - student_id 
        - grade

    - Course_enrolment: 
        - enrolment_id 
        - course_id 
        - student_id 
        - enrolment_date 

    - User: 
        - id: 
        - first_name: 
        - last_name 
        - email 
        - role (instructor, student)

    - Administrator: 
        - user_id

    - instructors 
        - instructor_id 

    - materials: 
        - material_id  
        - course_id 
        - title 
        - description 
        - file_path 
        - url 
        - created_at 
        - updated_at 


## TODO 

Move all the CRUD functions and utilities inside the service module