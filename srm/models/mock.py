import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Initialize Firebase Admin SDK
cred = credentials.Certificate("student-result-managemen-26370-firebase-adminsdk-wlt0w-bc2e3d728a.json")
firebase_admin.initialize_app(cred)

# Access Firestore database
db = firestore.client()

# Sample JSON data
json_data = """
[
        {
            "rollNumber": "001",
            "name": "John Doe",
            "marks": 85,
            "grade": "A"
        },
        {
            "rollNumber": "002",
            "name": "Jane Smith",
            "marks": 92,
            "grade": "A+"
        },
        {
            "rollNumber": "003",
            "name": "Bob Johnson",
            "marks": 78,
            "grade": "B"
        }
    ]
"""

# Convert JSON data to Python dictionary
data_dict = json.loads(json_data)

# Access the "entries" list in the dictionary and add each entry to Firestore

for entry in data_dict:
    db.collection("Results").add(entry)

print("Data added to Firestore successfully.")
