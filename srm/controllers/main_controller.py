from ..models.db import auth, get_all_students, get_all_lecturers, get_all_courses, get_all_results, get_all_result_disputes
from .auth_lib import sign_up, sign_in
from flask import Flask, render_template, request, redirect, url_for, flash
from srm import app


# app = Flask(__name__)
app.secret_key = 'a6d55b52545bc8146bc03cf61902f520'

result_disputes = get_all_result_disputes()
lecturers = get_all_lecturers()
courses = get_all_courses()
students = get_all_students()
results = get_all_results()



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the request is for login
        if 'loginEmail' in request.form and 'loginPassword' in request.form:
            email = request.form['loginEmail']
            password = request.form['loginPassword']
            # return "Yes"
            try:
                user = sign_in(email, password)
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
    return render_template('student_results.html', student_results=results)


@app.route('/student_information')
def student_information():
    return render_template('student_information.html', students=students)


@app.route('/course_management')
def course_management():
    return render_template('course_management.html', courses=courses)



@app.route('/lecturer_management')
def lecturer_management():
    return render_template('lecturer_management.html', lecturers=lecturers)



@app.route('/dispute')
def result_dispute():
    return render_template('result_dispute.html', result_disputes=result_disputes)
