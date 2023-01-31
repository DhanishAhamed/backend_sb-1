from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import string 
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///user.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80), unique=True, nullable=False)
    registerno = db.Column(db.String(80), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    batch = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.String(80), nullable=False)
    dept = db.Column(db.String(80),  nullable=False)
    blood = db.Column(db.String(10),  nullable=False)
    address = db.Column(db.String(120),  nullable=False)
    permcontact = db.Column(db.String(80), nullable=False)
    emergcontact = db.Column(db.String(80),  nullable=False)

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mon = db.Column(db.String(80), nullable=False)
    tue = db.Column(db.String(80), nullable=False)
    wed = db.Column(db.String(80), nullable=False)
    thu = db.Column(db.String(80), nullable=False)
    fri = db.Column(db.String(80), nullable=False)
# names = ["Aarav", "Aryan", "Aditi", "Aditya", "Akhil", "Alia", "Amrita", "Ananya", "Anika", "Anjali",          "Arjun", "Arnav", "Aryan", "Ashika", "Avni", "Ayesha", "Dhruv", "Divya", "Ishaan", "Ishika",          "Jhanvi", "Kavya", "Kritika", "Lakshmi", "Mahi", "Manav", "Meera", "Namrata", "Nivedita",          "Pooja", "Rajat", "Rhea", "Rohit", "Sakshi", "Samantha", "Sanjana", "Sarika", "Shivansh",          "Shruti", "Siddharth", "Simran", "Sonal", "Srija", "Srishti", "Tanya", "Tara", "Uma", "Vaishnavi"]
# surnames = ["Agarwal", "Ahuja", "Bhatia", "Chauhan", "Das", "Datta", "Desai", "Gandhi", "Gupta", "Jain",             "Kaur", "Khan", "Kumar", "Lal", "Mehta", "Mishra", "Nair", "Patel", "Rao", "Sharma",             "Shukla", "Singh", "Soni", "Tiwari", "Verma", "Varma"]
# blood_groups = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]

# with app.app_context():
#     db.create_all()
#     for i in range(1,51):
#         fullnamegen = random.choice(names)+" "+random.choice(surnames)+" "+random.choice(string.ascii_uppercase )
#         dobgen = str(random.randint(1, 28)) +"-"+str(random.randint(1, 12))+"-"+str(random.randint(2000, 2002))
#         registernogen = "RA2011026020"+str(i).zfill(3)
#         bloodgrpgen = random.choice(blood_groups)
#         random_number = random.randint(10000000000, 99999999999)
#         random_number2 = random.randint(10000000000, 99999999999)
#         letters = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
#         number = str(random.randint(1000, 9999))
#         usernamegen = letters + number
#         user = User(id=i,fullname = fullnamegen,registerno = registernogen,username =usernamegen,password = 12345678,batch="2020-2024",dob=dobgen,dept="CSE K",blood=bloodgrpgen,address="Chennai,Tamil Nadu",permcontact=random_number,emergcontact= random_number2)
#         db.session.add(user)
#         db.session.commit()
# subjects =["Database Management system","Compiler Design","Artifical Intelligence","Deep Learning","Fibre optics and Opto Electronics","Indian Art form","Seminar-2"]
# with app.app_context():
#     db.create_all()
#     for i in range(1,9):
#         timetable = Timetable(id=i,mon= random.choice(subjects),tue= random.choice(subjects),wed= random.choice(subjects),thu= random.choice(subjects),fri= random.choice(subjects),)
#         db.session.add(timetable)
#         db.session.commit()
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.password == password:
        return "Access granted", 200
    else:
        return "Access denied", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0')