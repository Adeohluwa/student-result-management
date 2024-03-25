from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.db import add_result, get_all_results, update_result, delete_result
from srm import app

# results_bp = Blueprint('results', __name__, template_folder='templates')

@app.route('/results')
def results():
    results = get_all_results()
    return render_template('results_management.html', results=results)

@app.route('/add_result', methods=['POST'])
def add_result_route():
    result_data = {
        'rollNumber': request.form['rollNumber'],
        'courseCode': request.form['courseCode'],
        'marks': int(request.form['marks']),
        'grade': request.form['grade']
    }
    new_result = add_result(result_data)
    flash('Result added successfully!', 'success')
    return redirect(url_for('results.results'))

# @results_bp.route('/update_result/<string:result_id>', methods=['POST'])
# def update_result_route(result_id):
#     updated_data = {
#         'rollNumber': request.form['rollNumber'],
#         'courseCode': request.form['courseCode'],
#         'marks': int(request.form['marks']),
#         'grade': request.form['grade']
#     }
#     update_result(result_id, updated_data)
#     flash('Result updated successfully!', 'success')
#     return redirect(url_for('results.results'))

@app.route('/delete_result/<string:result_id>')
def delete_result_route(result_id):
    delete_result(result_id)
    flash('Result deleted successfully!', 'success')
    return redirect(url_for('results.results'))
