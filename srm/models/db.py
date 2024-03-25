import firebase_admin 
from firebase_admin import credentials, auth, firestore


if not firebase_admin._apps:
    cred = credentials.Certificate("student-result-managemen-26370-firebase-adminsdk-wlt0w-bc2e3d728a.json")
    default_app = firebase_admin.initialize_app(cred)


db = firestore.client()


# Students

def add_student(student_data):
    doc_ref = db.collection('Students').document()
    student_data['id'] = doc_ref.id
    doc_ref.set(student_data)
    return student_data

def update_student(student_id, updated_data):
    doc_ref = db.collection('Students').document(student_id)
    doc_ref.update(updated_data)
    return doc_ref.get().to_dict()

def delete_student(student_id):
    doc_ref = db.collection('Students').document(student_id)
    doc_ref.delete()

def get_student(student_id):
    doc_ref = db.collection('Students').document(student_id)
    return doc_ref.get().to_dict()

def get_student_courses(student_id):
    doc_ref = db.collection('Students').document(student_id)
    return doc_ref.get().to_dict()

def get_all_students():
    students = db.collection('Students').stream()
    all_students = []

    for student in students:
        student_data = student.to_dict()
        student_data['id'] = student.id
        all_students.append(student_data)

    return all_students

# Courses

def add_course(course_data):
    doc_ref = db.collection('Courses').document()
    course_data['id'] = doc_ref.id
    doc_ref.set(course_data)
    return course_data

def update_course(course_id, updated_data):
    doc_ref = db.collection('Courses').document(course_id)
    doc_ref.update(updated_data)
    return doc_ref.get().to_dict()

def delete_course(course_id):
    doc_ref = db.collection('Courses').document(course_id)
    doc_ref.delete()
    return course_id

def get_course(course_id):
    doc_ref = db.collection('Courses').document(course_id)
    return doc_ref.get().to_dict()

def get_all_courses():
    courses = db.collection('Courses').stream()
    all_courses = []

    for course in courses:
        course_data = course.to_dict()
        course_data['id'] = course.id
        all_courses.append(course_data)

    return all_courses

# Lecturers

def add_lecturer(lecturer_data):
    doc_ref = db.collection('Lecturers').document()
    lecturer_data['id'] = doc_ref.id
    doc_ref.set(lecturer_data)
    return lecturer_data

def update_lecturer(lecturer_id, updated_data):
    doc_ref = db.collection('Lecturers').document(lecturer_id)
    doc_ref.update(updated_data)
    return doc_ref.get().to_dict()

def delete_lecturer(lecturer_id):
    doc_ref = db.collection('Lecturers').document(lecturer_id)
    doc_ref.delete()
    return lecturer_id

def get_lecturer(lecturer_id):
    doc_ref = db.collection('Lecturers').document(lecturer_id)
    return doc_ref.get().to_dict()

def get_lecturer_courses(lecturer_id):
    doc_ref = db.collection('Lecturers').document(lecturer_id)
    return doc_ref.get().to_dict()

def get_all_lecturers():
    lecturers = db.collection('Lecturers').stream()
    all_lecturers = []

    for lecturer in lecturers:
        lecturer_data = lecturer.to_dict()
        lecturer_data['id'] = lecturer.id
        all_lecturers.append(lecturer_data)

    return all_lecturers

# Result Disputes

def add_dispute(dispute_data):
    doc_ref = db.collection('Disputes').document()
    dispute_data['id'] = doc_ref.id
    doc_ref.set(dispute_data)
    return dispute_data

def update_dispute(dispute_id, updated_data):
    doc_ref = db.collection('Disputes').document(dispute_id)
    doc_ref.update(updated_data)
    return doc_ref.get().to_dict()

def delete_dispute(dispute_id):
    doc_ref = db.collection('Disputes').document(dispute_id)
    doc_ref.delete()

def get_dispute(dispute_id):
    doc_ref = db.collection('Disputes').document(dispute_id)
    return doc_ref.get().to_dict()

def get_all_disputes():
    disputes = db.collection('Disputes').stream()
    all_disputes = []

    for dispute in disputes:
        dispute_data = dispute.to_dict()
        dispute_data['id'] = dispute.id
        all_disputes.append(dispute_data)

    return all_disputes


# Results

def add_result(result_data):
    doc_ref = db.collection('Results').document()
    result_data['id'] = doc_ref.id
    doc_ref.set(result_data)
    return result_data

def update_result(result_id, updated_data):
    doc_ref = db.collection('Results').document(result_id)
    doc_ref.update(updated_data)
    return doc_ref.get().to_dict()

def delete_result(result_id):
    doc_ref = db.collection('Results').document(result_id)
    doc_ref.delete()

def get_result(result_id):
    doc_ref = db.collection('Results').document(result_id)
    return doc_ref.get().to_dict()

def get_all_results():
    results = db.collection('Results').stream()
    all_results = []

    for result in results:
        result_data = result.to_dict()
        result_data['id'] = result.id
        all_results.append(result_data)

    return all_results

def get_results_by_student_id(student_id):
    results = db.collection('Results').where('student_id', '==', student_id).stream()
    student_results = []

    for result in results:
        result_data = result.to_dict()
        result_data['id'] = result.id
        student_results.append(result_data)

    return student_results

def get_results_by_course_id(course_id):
    results = db.collection('Results').where('course_id', '==', course_id).stream()
    course_results = []

    for result in results:
        result_data = result.to_dict()
        result_data['id'] = result.id
        course_results.append(result_data)

    return course_results
