from ..models.db import auth
from flask import Flask, render_template, request, redirect, url_for, flash
from app import app
import time


# app = Flask(__name__)
app.secret_key = 'a6d55b52545bc8146bc03cf61902f520'




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the request is for login
        if 'loginEmail' in request.form and 'loginPassword' in request.form:
            email = request.form['loginEmail']
            password = request.form['loginPassword']
            # return "Yes"
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                flash('Login successful!', 'success')
                # Redirect to the desired page after successful login
                return redirect(url_for('index'))
            except Exception as e:
                error_message = str(e)
                flash(f'Login failed: {error_message}', 'danger')

        # Check if the request is for signup
        elif 'signupEmail' in request.form and 'signupPassword' in request.form and 'signupConfirmPassword' in request.form:
            email = request.form['signupEmail']
            password = request.form['signupPassword']
            confirm_password = request.form['signupConfirmPassword']
            if password == confirm_password:
                try:
                    user = auth.create_user(email=email, password=password)
                    flash('Signup successful!', 'success')
                    # Redirect to the desired page after successful signup
                    return redirect(url_for('index'))
                except Exception as e:
                    error_message = str(e)
                    flash(f'Signup failed: {error_message}', 'danger')
            else:
                flash('Passwords do not match', 'danger')

    # Render the 'login.html' template for GET requests
    return render_template('login.html')
# def index():
#     if request.method == 'POST':
#         if 'email' in request.form and 'password' in request.form:
#             email = request.form['email']
#             password = request.form['password']
#             print(f" the pass is {password}")
#             try:
#                 user = auth.create_user(email=email, password=password)
#                 flash('Signup successful!', 'success')
#                 time.sleep(3)
#                 return redirect(url_for('index'))
#             except Exception as e:
#                 error_message = str(e)
#                 flash(f'Signup failed: {error_message}', 'danger')
#             else:
#                 flash('Passwords do not match', 'danger')

#             # return email
#     # password = request.form['loginPassword']
#     # email = request.form['email']
#     # password = request.form['password']
#     # return email
#     # return 

#     # Render the 'base.html' template
#     return render_template('login.html')

# @app.route('/signup', methods=['GET','POST'])
# def signup():
#     # Render the 'base.html' template
#     email = request.form['email']
#     password = request.form['password']
#     try:
#         flash('Signup successful!', 'success')
#         user = auth.create_user_with_email_and_password(email, password)
#         return redirect(url_for('index'))
#     except Exception as e:
#         error_message = str(e)
#         flash(f'Signup failed: {error_message}', 'danger')
#     else:
#         flash('Passwords do not match', 'danger')
#     print(email)
#     email = request.form['email']
#     password = request.form['password']
#     return f"{email}"
#     print(password)
#     return render_template('login.html')



# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if 'loginEmail' in request.form and 'loginPassword' in request.form:
#             email = request.form['loginEmail']
#             password = request.form['loginPassword']
#             try:
#                 user = auth.sign_in_with_email_and_password(email, password)
#                 flash('Login successful!', 'success')
#                 return redirect(url_for('index'))
#             except Exception as e:
#                 error_message = str(e)
#                 flash(f'Login failed: {error_message}', 'danger')
#         elif 'signupEmail' in request.form and 'signupPassword' in request.form and 'signupConfirmPassword' in request.form:
#             email = request.form['signupEmail']
#             password = request.form['signupPassword']
#             confirm_password = request.form['signupConfirmPassword']
#             if password == confirm_password:
#                 try:
#                     user = auth.create_user_with_email_and_password(email, password)
#                     flash('Signup successful!', 'success')
#                     return redirect(url_for('index'))
#                 except Exception as e:
#                     error_message = str(e)
#                     flash(f'Signup failed: {error_message}', 'danger')
#             else:
#                 flash('Passwords do not match', 'danger')
#     return render_template('index.html')








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
