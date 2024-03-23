from flask import Flask, render_template

app = Flask(__name__)

# Import controllers
from app.controllers import main_controller

if __name__ == '__main__':
    app.run(debug=True)