from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  email = Column(String, unique=True)
  password = Column(String)
  role = Column(String)


class Product(db.Model):
  __tablename__ = 'products'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
  cost_price = Column(Integer)
  selling_price = Column(Integer)
  qty = Column(Integer)


class Order(db.Model):
  __tablename__ = 'orders'
  id = Column(Integer, primary_key=True, autoincrement=True)
  type = Column(String)  # incoming, outgoing
  product_id = Column(Integer, ForeignKey('products.id'))
  qty = Column(Integer)
  status = Column(String)  # pending, delivered
  date_placed = Column(DateTime)
  date_delivered = Column(DateTime)
  supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=True)  # null for outgoing orders
  client_id = Column(Integer, ForeignKey('clients.id'), nullable=True)  # null for incoming orders


class Supplier(db.Model):
  __tablename__ = 'suppliers'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)


class Client(db.Model):
  __tablename__ = 'clients'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String)
