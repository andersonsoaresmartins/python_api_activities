from models import Persons


def insertPersons():
    person = Persons(name='Anderson', age=40)
    person.save()


def searchPersons():
    person = Persons.query.all()
    print(person)

    
    person = Persons.query.filter_by(name='Anderson')

    for p in person:
        print('Name:', p.name, 'Age:', p.age)


    person = Persons.query.filter_by(name='Anderson').first()
    print(person.name)

    persons = Persons.query.all()
    for p in persons:
        print('Name:', p.name, 'Age:', p.age)


def modifyPersons():
    person = Persons.query.filter_by(name='Anderson').first()
    person.age = 45
    person.save()


def deletePersons():
    person = Persons.query.filter_by(name='Anderson').first()
    person.delete()


if __name__ == '__main__':
   insertPersons()
   #modifyPersons()
   searchPersons()
   #deletePersons()
   