from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base
# from sqlalchemy.ext.declarative import declarative_base


# Conexão com o Banco de Dados
engine = create_engine('sqlite:///activities.db')

# Sessão para acesso ao Banco de Dados
db_session = scoped_session(sessionmaker(autocommit=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


# Classe Persons
class Persons(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), index=True)
    age = Column(Integer)

    # Representação da classe Persons
    def __repr__(self):
        return '<People {}>'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# Classe Persons


class Activities(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    person_id = Column(Integer, ForeignKey('persons.id'))
    person = relationship("Persons")

    def __repr__(self):
        return '<Activities {}>'.format(self.name)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    passwd = Column(String(20))

    def __repr__(self):
        return '<Users {}>' .format(self.login)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
