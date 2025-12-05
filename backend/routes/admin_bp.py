from flask import Blueprint, render_template
from utils import role_required
from models import *

admin_bp = Blueprint("admin_bp", __name__, url_prefix='/admin')


@admin_bp.route('/home')
@role_required('admin')
def admin_home():
  return render_template('admin/index.html')


@admin_bp.route('/products')
@role_required('admin')
def products():
  products = Product.query.all()
  return render_template('admin/products.html', products=products)


@admin_bp.route('/orders')
@role_required('admin')
def orders():
  orders = Order.query.all()
  return render_template('admin/orders.html', orders=orders)


@admin_bp.route('/customers')
@role_required('admin')
def customers():
  customers = Customer.query.all()
  return render_template('admin/customers.html', customers=customers)


@admin_bp.route('/suppliers')
@role_required('admin')
def suppliers():
  suppliers = Supplier.query.all()
  return render_template('admin/suppliers.html', suppliers=suppliers)
