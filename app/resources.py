from flask import request
from flask_restful import Resource
from app import db
from app.models import HouseHelp, Client, Assignment, Payment

# HouseHelp Resource
class HouseHelpResource(Resource):
    def get(self, id=None):
        if id:
            househelp = HouseHelp.query.get_or_404(id)
            return househelp.to_dict(), 200
        househelps = HouseHelp.query.all()
        return [househelp.to_dict() for househelp in househelps], 200

    def post(self):
        data = request.get_json()
        new_househelp = HouseHelp(
            name=data['name'],
            gender=data['gender'],
            county=data['county'],
            next_of_kin=data['next_of_kin'],
            experience=data['experience'],
            salary_expectation=data['salary_expectation'],
            preferred_location=data['preferred_location'],
            age=data['age'],
            profile_pic=data['profile_pic']
        )
        db.session.add(new_househelp)
        db.session.commit()
        return new_househelp.to_dict(), 201

    def put(self, id):
        data = request.get_json()
        househelp = HouseHelp.query.get_or_404(id)
        househelp.name = data['name']
        househelp.gender = data['gender']
        househelp.county = data['county']
        househelp.next_of_kin = data['next_of_kin']
        househelp.experience = data['experience']
        househelp.salary_expectation = data['salary_expectation']
        househelp.preferred_location = data['preferred_location']
        househelp.age = data['age']
        househelp.profile_pic = data['profile_pic']
        db.session.commit()
        return househelp.to_dict(), 200

    def delete(self, id):
        househelp = HouseHelp.query.get_or_404(id)
        db.session.delete(househelp)
        db.session.commit()
        return '', 204

# Client Resource
class ClientResource(Resource):
    def get(self, id=None):
        if id:
            client = Client.query.get_or_404(id)
            return client.to_dict(), 200
        clients = Client.query.all()
        return [client.to_dict() for client in clients], 200

    def post(self):
        data = request.get_json()
        new_client = Client(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            address=data['address']
        )
        db.session.add(new_client)
        db.session.commit()
        return new_client.to_dict(), 201

    def put(self, id):
        data = request.get_json()
        client = Client.query.get_or_404(id)
        client.name = data['name']
        client.email = data['email']
        client.phone = data['phone']
        client.address = data['address']
        db.session.commit()
        return client.to_dict(), 200

    def delete(self, id):
        client = Client.query.get_or_404(id)
        db.session.delete(client)
        db.session.commit()
        return '', 204

# Assignment Resource
class AssignmentResource(Resource):
    def get(self, id=None):
        if id:
            assignment = Assignment.query.get_or_404(id)
            return assignment.to_dict(), 200
        assignments = Assignment.query.all()
        return [assignment.to_dict() for assignment in assignments], 200

    def post(self):
        data = request.get_json()
        new_assignment = Assignment(
            client_id=data['client_id'],
            househelp_id=data['househelp_id'],
            salary=data['salary']
        )
        db.session.add(new_assignment)
        db.session.commit()
        return new_assignment.to_dict(), 201

    def put(self, id):
        data = request.get_json()
        assignment = Assignment.query.get_or_404(id)
        assignment.client_id = data['client_id']
        assignment.househelp_id = data['househelp_id']
        assignment.salary = data['salary']
        db.session.commit()
        return assignment.to_dict(), 200

    def delete(self, id):
        assignment = Assignment.query.get_or_404(id)
        db.session.delete(assignment)
        db.session.commit()
        return '', 204

# Payment Resource
class PaymentResource(Resource):
    def get(self, id=None):
        if id:
            payment = Payment.query.get_or_404(id)
            return payment.to_dict(), 200
        payments = Payment.query.all()
        return [payment.to_dict() for payment in payments], 200

    def post(self):
        data = request.get_json()
        new_payment = Payment(
            assignment_id=data['assignment_id'],
            amount=data['amount']
        )
        db.session.add(new_payment)
        db.session.commit()
        return new_payment.to_dict(), 201

    def put(self, id):
        data = request.get_json()
        payment = Payment.query.get_or_404(id)
        payment.amount = data['amount']
        db.session.commit()
        return payment.to_dict(), 200

    def delete(self, id):
        payment = Payment.query.get_or_404(id)
        db.session.delete(payment)
        db.session.commit()
        return '', 204

