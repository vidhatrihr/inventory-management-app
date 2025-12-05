from flask import Flask, render_template, redirect
from models import db, User
from populate_db import populate_db
from flask_login import LoginManager, current_user
from flask_debugtoolbar import DebugToolbarExtension

from routes.auth_bp import auth_bp
from routes.admin_bp import admin_bp
from routes.manager_bp import manager_bp

app = Flask(__name__)
app.debug = True
app.secret_key = '12345'  # for flask login sessions

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(manager_bp)

# DebugToolbarExtension(app)

# setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

# create tables and populate
with app.app_context():
  db.create_all()
  if User.query.count() == 0:
    populate_db()


# setup flask login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
  return User.query.filter_by(id=user_id).first()


@app.route('/')
def index():
  if current_user.is_authenticated:
    if current_user.role == 'admin':
      return redirect('/admin/home')
    elif current_user.role == 'manager':
      return redirect('/manager/home')

  users_count = User.query.count()
  return render_template('index.html', users_count=users_count)


if __name__ == '__main__':
  app.run(debug=True)
