from ..models.db import auth, get_all_students, get_all_lecturers, get_all_courses, get_all_results, get_all_disputes
from .auth_lib import sign_up, sign_in
from flask import Flask, render_template, request, redirect, url_for, flash
from srm import app
from .courses_controllers import courses


# app = Flask(__name__)
app.secret_key = 'a6d55b52545bc8146bc03cf61902f520'

result_disputes = get_all_disputes()
lecturers = get_all_lecturers()
courses = get_all_courses()
students = get_all_students()
results = get_all_results()

studentEmail="student@gmail.com"
studentPassword="student"


lecturerEmail="lecturer@gmail.com"
lecturerPassword="lecturer"




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the request is for login
        if 'loginEmail' in request.form and 'loginPassword' in request.form:
            email = request.form['loginEmail']
            password = request.form['loginPassword']
            # return "Yes"


            if email == studentEmail and password == studentPassword:
                try:
                    user = sign_in(email, password)
                    flash('Login successful!', 'success')
                    # Redirect to the desired page after successful login
                    return render_template("student_dashboard.html")
                except Exception as e:
                    error_message = str(e)
                    flash(f'Login failed: {error_message}', 'danger')

 

            


            if email == lecturerEmail and password == lecturerPassword:
                try:
                    user = sign_in(email, password)
                    flash('Login successful!', 'success')
                    # Redirect to the desired page after successful login
                    return render_template("lecturer_dashboard.html")
                except Exception as e:
                    error_message = str(e)
                    flash(f'Login failed: {error_message}', 'danger')



            try:
                user = sign_in(email, password)
                flash('Login successful!', 'success')
                # Redirect to the desired page after successful login
                return redirect(url_for('courses'))
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


@app.route('/studentDashboard')
def studentDashboard():
    # Render the template with the results
    return render_template('student_dashboard.html', courses=courses, students=students)

@app.route('/lecturerDashboard')
def lecturerDashboard():
    # Render the template with the results
    return render_template('lecturer_dashboard.html', courses=courses, students=students)
