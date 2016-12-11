from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

def getCurrentTime():
	return datetime.datetime.now()


class User(Base):
	"""docstring for User"""
	__tablename__ = "user"
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)

	@property
	def serialize(self):
		"""Returns json"""
		return {
			'id': self.id,
			'name': self.name,
			'email': self.email
		}


class Category(Base):
	"""docstring for Category"""
	__tablename__ = 'category'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	user_id = Column(String(250), ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		"""returns json"""
		return {
			'id': self.id,
			'name': self.name,
			'user_id': self.name
		}

class Item(Base):
	"""docstring for Item"""
	__tablename__= 'item'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	description = Column(String(500))
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'category_id': self.category_id,
			'user_id': self.user_id
		}

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)
		

		
		