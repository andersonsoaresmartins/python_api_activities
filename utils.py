from models import Persons, Users


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


def insertUser(login, passwd):
    user = Users(login=login, passwd=passwd)
    user.save()


def showUsers():
    users = Users.query.all()
    print(users)




if __name__ == '__main__':
   #insertPersons()
   #modifyPersons()
   #searchPersons()
   #deletePersons()
   insertUser('admin', 'admin')
   showUsers()
