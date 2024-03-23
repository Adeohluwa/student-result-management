from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.db import add_lecturer, get_all_lecturers, update_lecturer, delete_lecturer

lecturers_bp = Blueprint('lecturers', __name__, template_folder='templates')

@lecturers_bp.route('/lecturers')
def lecturers():
    lecturers = get_all_lecturers()
    return render_template('lecturer_management.html', lecturers=lecturers)

@lecturers_bp.route('/add_lecturer', methods=['POST'])
def add_lecturer_route():
    lecturer_data = {
        'lecturerId': request.form['lecturerId'],
        'lecturerName': request.form['lecturerName'],
        'lecturerEmail': request.form['lecturerEmail']
    }
    new_lecturer = add_lecturer(lecturer_data)
    flash('Lecturer added successfully!', 'success')
    return redirect(url_for('lecturers.lecturers'))

@lecturers_bp.route('/update_lecturer/<string:lecturer_id>', methods=['POST'])
def update_lecturer_route(lecturer_id):
    updated_data = {
        'lecturerId': request.form['lecturerId'],
        'lecturerName': request.form['lecturerName'],
        'lecturerEmail': request.form['lecturerEmail']
    }
    update_lecturer(lecturer_id, updated_data)
    flash('Lecturer updated successfully!', 'success')
    return redirect(url_for('lecturers.lecturers'))

@lecturers_bp.route('/delete_lecturer/<string:lecturer_id>')
def delete_lecturer_route(lecturer_id):
    delete_lecturer(lecturer_id)
    flash('Lecturer deleted successfully!', 'success')
    return redirect(url_for('lecturers.lecturers'))
