from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Модель для таблицы Users
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    
    # Связь с таблицей Posts
    posts = relationship('Post', back_populates='user')

# Модель для таблицы Posts
class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Связь с пользователем
    user = relationship('User', back_populates='posts')

# Создание соединения с базой данных SQLite
engine = create_engine('sqlite:///example.db', echo=True)

# Создание таблиц в базе данных
Base.metadata.create_all(engine)