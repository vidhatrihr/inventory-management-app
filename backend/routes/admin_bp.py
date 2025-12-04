from flask import Blueprint, render_template
from utils import role_required
from models import Product

admin_bp = Blueprint("admin_bp", __name__, url_prefix='/admin')


@admin_bp.route('/home')
@role_required('admin')
def admin_home():
  return render_template('admin/index.html')


@admin_bp.route('/products')
@role_required('admin')
def products():
  return ['apple', 'banana', 'kiwi']
