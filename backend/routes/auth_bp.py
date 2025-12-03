from flask import Blueprint, render_template, redirect, request
from models import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user

auth_bp = Blueprint("auth_bp", __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
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


@auth_bp.route('/logout')
def logout():
  logout_user()
  return redirect('/login')
