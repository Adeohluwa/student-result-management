from flask import render_template, request, url_for
from app import app

@app.route('/')
def index():
    # Render the 'base.html' template
    return render_template('base.html')

@app.route('/student_results')
def student_results():
    student_results = [
        {
            'rollNumber': '001',
            'name': 'John Doe',
            'marks': 85,
            'grade': 'A'
        },
        {
            'rollNumber': '002',
            'name': 'Jane Smith',
            'marks': 92,
            'grade': 'A+'
        },
        {
            'rollNumber': '003',
            'name': 'Bob Johnson',
            'marks': 78,
            'grade': 'B'
        }
    ]
    return render_template('student_results.html', student_results=student_results)

@app.route('/student_information')
def student_information():
    students = [
        {
            'id': 1,
            'rollNumber': '001',
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        },
        {
            'id': 2,
            'rollNumber': '002',
            'name': 'Jane Smith',
            'email': 'jane.smith@example.com'
        },
        {
            'id': 3,
            'rollNumber': '003',
            'name': 'Bob Johnson',
            'email': 'bob.johnson@example.com'
        }
    ]
    return render_template('student_information.html', students=students)
@app.route('/course_management')
def course_management():
    courses = [
        {
            'id': 1,
            'courseCode': 'CSE101',
            'courseName': 'Introduction to Programming',
            'courseInstructor': 'Dr. Jane Smith'
        },
        {
            'id': 2,
            'courseCode': 'CSE201',
            'courseName': 'Data Structures and Algorithms',
            'courseInstructor': 'Dr. John Doe'
        },
        {
            'id': 3,
            'courseCode': 'CSE301',
            'courseName': 'Database Management Systems',
            'courseInstructor': 'Dr. Alice Williams'
        }
    ]
    return render_template('course_management.html', courses=courses)

@app.route('/lecturer_management')
def lecturer_management():
    lecturers = [
        {
            'id': 1,
            'lecturerId': 'L001',
            'lecturerName': 'Dr. John Doe',
            'lecturerEmail': 'john.doe@example.com'
        },
        {
            'id': 2,
            'lecturerId': 'L002',
            'lecturerName': 'Dr. Jane Smith',
            'lecturerEmail': 'jane.smith@example.com'
        },
        {
            'id': 3,
            'lecturerId': 'L003',
            'lecturerName': 'Dr. Alice Williams',
            'lecturerEmail': 'alice.williams@example.com'
        }
    ]
    return render_template('lecturer_management.html', lecturers=lecturers)

@app.route('/dispute')
def result_dispute():
    result_disputes = [
        {
            'roll_number': '001',
            'name': 'John Doe',
            'course': 'Mathematics',
            'reason': 'Miscalculation of marks',
            'status': 'Pending'
        },
        {
            'roll_number': '002',
            'name': 'Jane Smith',
            'course': 'English',
            'reason': 'Missing assignment',
            'status': 'Approved'
        },
        {
            'roll_number': '003',
            'name': 'Bob Johnson',
            'course': 'Science',
            'reason': 'Miscalculation of grade',
            'status': 'Rejected'
        }
    ]
    return render_template('result_dispute.html', result_disputes=result_disputes)
