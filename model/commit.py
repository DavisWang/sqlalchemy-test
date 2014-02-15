from base import Base
from sqlalchemy import Column, Integer, DateTime, String

class Commit(Base):
	__tablename__ = 'commit'

	id = Column(Integer, primary_key=True)
	commit_hash = Column(String)
	commit_date = Column(DateTime)
	user_id = Column(Integer)