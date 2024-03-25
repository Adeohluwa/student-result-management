from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.db import add_student, get_all_students, update_student, delete_student
from srm import app

# students_bp = Blueprint('students', __name__, template_folder='templates')

@app.route('/students')
def students():
    students = get_all_students()
    return render_template('student_information.html', students=students)

@app.route('/add_student', methods=['POST'])
def add_student_route():
    student_data = {
        'rollNumber': request.form['rollNumber'],
        'name': request.form['name'],
        'email': request.form['email']
    }
    new_student = add_student(student_data)
    flash('Student added successfully!', 'success')
    return redirect(url_for('students'))

# @students_bp.route('/update_student/<string:student_id>', methods=['POST'])
# def update_student_route(student_id):
#     updated_data = {
#         'rollNumber': request.form['rollNumber'],
#         'name': request.form['name'],
#         'email': request.form['email']
#     }
#     update_student(student_id, updated_data)
#     flash('Student updated successfully!', 'success')
#     return redirect(url_for('students.students'))

@app.route('/delete_student/<string:student_id>', methods=['POST'])
def delete_student_route(student_id):
    delete_student(student_id)
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('students'))
