from datetime import datetime
from app import db  # Import db from app (only after it is defined in create_app)

# HouseHelp model
class HouseHelp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    county = db.Column(db.String(120), nullable=False)
    next_of_kin = db.Column(db.String(120))
    experience = db.Column(db.String(255))
    salary_expectation = db.Column(db.Integer)
    preferred_location = db.Column(db.String(120))
    age = db.Column(db.Integer)
    profile_pic = db.Column(db.String(120))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'county': self.county,
            'next_of_kin': self.next_of_kin,
            'experience': self.experience,
            'salary_expectation': self.salary_expectation,
            'preferred_location': self.preferred_location,
            'age': self.age,
            'profile_pic': self.profile_pic
        }

# Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

# Assignment model
class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    househelp_id = db.Column(db.Integer, db.ForeignKey('house_help.id'), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.utcnow)
    end_date = db.Column(db.DateTime)
    salary = db.Column(db.Integer, nullable=False)

    client = db.relationship('Client', backref=db.backref('assignments', lazy=True))
    househelp = db.relationship('HouseHelp', backref=db.backref('assignments', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'client_id': self.client_id,
            'househelp_id': self.househelp_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'salary': self.salary
        }

# Payment model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('assignment.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    assignment = db.relationship('Assignment', backref=db.backref('payments', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'assignment_id': self.assignment_id,
            'amount': self.amount,
            'date': self.date
        }




