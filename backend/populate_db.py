from werkzeug.security import generate_password_hash
from models import *


def populate_db():
  admin = User(
      name='Admin',
      email='admin@example.com',
      password=generate_password_hash('12345'),
      role='admin'
  )
  db.session.add(admin)

  manager = User(
      name='Manager',
      email='manager@example.com',
      password=generate_password_hash('12345'),
      role='manager'
  )
  db.session.add(manager)

  db.session.commit()
