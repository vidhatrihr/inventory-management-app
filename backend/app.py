from flask import Flask, render_template, request, redirect
from models import db, User
from populate_db import populate_db
from flask_login import LoginManager, login_user, logout_user, current_user
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = '12345'  # for flask login sessions

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


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None

  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):
      login_user(user)
      return redirect('/')

    error = 'Email or password incorrect, try again!'

  return render_template('login.html', error=error)


@app.route('/logout')
def logout():
  logout_user()
  return redirect('/login')


@app.route('/admin/home')
def admin_home():
  return render_template('admin/index.html')


@app.route('/manager/home')
def manager_home():
  return render_template('manager/index.html')


if __name__ == '__main__':
  app.run(debug=True)
