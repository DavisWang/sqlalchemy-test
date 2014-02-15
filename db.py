import sys
import sqlalchemy
from datetime import datetime
from model.commit import Commit
from model.user import User

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def initDB():
	engine = create_engine('mysql://root_davis:davis_dev@localhost/davis_db')
	Session = sessionmaker(bind=engine)
	return Session()

def process():
	print len(sys.argv)
	print str(sys.argv)

	#aid = 123
	#chash = '2j2j3j4h4hsh4h22232d'
	#cdate = "2014-02-13 12:34:45"

	# cdate = datetime.strptime(cdate, '%Y-%m-%d %H:%M:%S')
	session = initDB()
	# commit = Commit(commit_hash=chash, commit_date=cdate, user_id=aid)
	for i in xrange(100):
		fname = 'davis'+str(i)
		lname = 'wang'+str(i)

		user = User(first_name=fname, last_name=lname)
		session.add(user)
	session.commit()

process()





