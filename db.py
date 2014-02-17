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

  session = initDB()
  #add if user exists in table don't add
  commit = Commit(commit_hash=sys.argv[1], commit_date=datetime.strptime(sys.argv[3], '%Y-%m-%d %H:%M:%S -0800'), user_id=sys.argv[2])
  session.add(commit)
  session.commit()
  print "Done DB work"         

process()





