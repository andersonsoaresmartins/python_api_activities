from flask import Flask, request
from flask_restful import Resource, Api
from models import Persons, Activities


app = Flask(__name__)
api = Api(app)


class Person(Resource):
    def get(self, name):
        person = Persons.query.filter_by(name=name).first()

        try:
            response = {
                'name': person.name,
                'age': person.age,
                'id': person.id
            }

        except AttributeError:
            response = {
                'status': 'error',
                'message': 'Person do not finded!'
            }

        return response

    def put(self, name):
        person = Persons.query.filter_by(name=name).first()
        data = request.json

        if 'name' in data:
            person.name = data['name']

        if 'age' in data:
            person.age = data['age']

        person.save()

        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }

        return response

    def delete(self, name):
        person = Persons.query.filter_by(name=name).first()
        message = 'Person {} deleted was sucessfully!'.format(person.name)
        person.delete()
        return {
            'status': 'success',
            'message': message
        }


class PersonsList(Resource):
    def get(self):
        persons = Persons.query.all()
        response = [{'id': i.id, 'name': i.name, 'age': i.age}
                    for i in persons]
        return response


    def post(self):
        data = request.json
        person = Persons(name=data['name'], age=data['age'])
        person.save()
        response = {
            'id': person.id,
            'name': person.name,
            'age': person.age
        }

        return response


class ActivitiesList(Resource):
    def get(self):
        activities = Activities.query.all()
        response = [{'id': i.id, 'name': i.name, 'person':i.person} for i in activities]
        return response

    def post(self):
        data = request.json
        person = Persons.query.filter_by(name=data['person']).first()
        activity = Activities(name=data['name'], person=person)
        activity.save()
        response = {
            'person': activity.person.name,
            'name': activity.name,
            'id': activity.id
        }

        return response

api.add_resource(Person, '/person/<string:name>/')
api.add_resource(PersonsList, '/persons/')
api.add_resource(ActivitiesList, '/activities/')


if __name__ == '__main__':
    app.run(debug=True)
