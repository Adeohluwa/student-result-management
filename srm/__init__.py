from flask import Flask, render_template

app = Flask(__name__)

# Import controllers
from srm.controllers import main_controller
from srm.controllers import students_controllers
from srm.controllers import lecturers_controllers
from srm.controllers import courses_controllers
from srm.controllers import results_controllers
from srm.controllers import disputes_controllers

if __name__ == '__main__':
    app.run(debug=True)