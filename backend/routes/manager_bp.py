from flask import Blueprint, render_template
from utils import role_required

manager_bp = Blueprint("manager_bp", __name__, url_prefix='/manager')


@manager_bp.route('/home')
@role_required('manager')
def manager_home():
  return render_template('manager/index.html')
