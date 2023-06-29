from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from models.database import engine, Session

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(50))

    @staticmethod
    def user_exists(username):
        session = Session()
        user = session.query(UserModel).filter_by(username=username).first()
        session.close()
        return user

    @staticmethod
    def register_user(username, password):
        user = UserModel(username=username, password=password)

        # Adiciona os usuários à sessão e persiste no banco de dados
        session = Session()
        session.add(user)
        session.commit()

    @staticmethod
    def authenticate_user(username, password):
        session = Session()
        user = session.query(UserModel).filter_by(username=username, password=password).first()
        session.close()
        return user

Base.metadata.create_all(engine)
