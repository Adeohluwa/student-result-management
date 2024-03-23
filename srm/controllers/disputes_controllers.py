from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models.db import add_dispute, get_all_disputes, update_dispute, delete_dispute

disputes_bp = Blueprint('disputes', __name__, template_folder='templates')

@disputes_bp.route('/disputes')
def disputes():
    disputes = get_all_disputes()
    return render_template('disputes/result_dispute.html', disputes=disputes)

@disputes_bp.route('/add_dispute', methods=['POST'])
def add_dispute_route():
    dispute_data = {
        'rollNumber': request.form['rollNumber'],
        'courseCode': request.form['courseCode'],
        'reason': request.form['reason'],
        'status': 'pending'
    }
    new_dispute = add_dispute(dispute_data)
    flash('Dispute added successfully!', 'success')
    return redirect(url_for('disputes.disputes'))

@disputes_bp.route('/update_dispute/<string:dispute_id>', methods=['POST'])
def update_dispute_route(dispute_id):
    updated_data = {
        'rollNumber': request.form['rollNumber'],
        'courseCode': request.form['courseCode'],
        'reason': request.form['reason'],
        'status': request.form['status']
    }
    update_dispute(dispute_id, updated_data)
    flash('Dispute updated successfully!', 'success')
    return redirect(url_for('disputes.disputes'))

@disputes_bp.route('/delete_dispute/<string:dispute_id>')
def delete_dispute_route(dispute_id):
    delete_dispute(dispute_id)
    flash('Dispute deleted successfully!', 'success')
    return redirect(url_for('disputes.disputes'))
