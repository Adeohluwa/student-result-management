from flask import render_template, request, redirect, url_for, flash
from ..models.db import add_course, get_all_courses, update_course, delete_course
from srm import app

# courses_bp = Blueprint('courses', __name__, template_folder='templates')

@app.route('/courses')
def courses():
    courses = get_all_courses()
    return render_template('course_management.html', courses=courses)

@app.route('/add_course', methods=['POST'])
def add_course_route():
    # return request.form
    course_data = {
        'courseCode': request.form['courseCode'],
        'courseName': request.form['courseName'],
        'courseInstructor': request.form['courseInstructor']
    }
    new_course = add_course(course_data)
    flash('Course added successfully!', 'success')
    return redirect(url_for('courses'))

@app.route('/update_course/<string:course_id>', methods=['POST'])
def update_course_route(course_id):
    updated_data = {
        'courseCode': request.form['courseCode'],
        'courseName': request.form['courseName'],
        'courseInstructor': request.form['courseInstructor']
    }
    update_course(course_id, updated_data)
    flash('Course updated successfully!', 'success')
    return redirect(url_for('courses'))

@app.route('/delete_course/<string:course_id>',methods=['POST'])
def delete_course_route(course_id):
    delete_course(course_id)
    flash('Course deleted successfully!', 'success')
    return redirect(url_for('courses'))