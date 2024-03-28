from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text, MetaData, TIMESTAMP, JSON, Boolean
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel
from sqlalchemy import DECIMAL as Decimal

Base = declarative_base()
class Role(Base):
    __tablename__ = "role"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    permissions = Column(JSON)
    
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey("role.id"))
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)

class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), nullable=True)
    address = Column(String(100), nullable=True)
    phone = Column(String(15), unique=True, nullable=True)

class Courier(Base):
    __tablename__ = "couriers"

    courier_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"), nullable=True)
    name = Column(String(20))
    phone_number = Column(String(15))
    rating = Column(Decimal(3, 2), default=1)
    status = Column(String(10), default="Busy")
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=True)
    geolocation = Column(Integer)

class Restaurant(Base):
    __tablename__ = "restaurants"

    rest_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30))
    address = Column(String(40))
    type = Column(String(50))
    phone_number = Column(String(15))
    working_time = Column(String(50))

class Product(Base):
    __tablename__ = "products"

    prod_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    rest_id = Column(Integer, ForeignKey("restaurants.rest_id"))
    name = Column(String(50))
    price = Column(Decimal(8, 2))
    description = Column(Text, nullable=True)
    category = Column(String(50))

class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("clients.client_id"))
    courier_id = Column(Integer, ForeignKey("couriers.courier_id"))
    rest_id = Column(Integer, ForeignKey("restaurants.rest_id"))
    status = Column(String(20))
    date = Column(DateTime)

class OrderDetail(Base):
    __tablename__ = "order_details"

    order_det_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    comment = Column(Text(255))

class OrderProd(Base):
    __tablename__ = "order_prods"
    order_prods_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.order_id"))
    prod_id = Column(Integer, ForeignKey("products.prod_id"))
    prods_quantity = Column(Integer)
    order_price = Column(Decimal(8, 2))

 #    order_id integer(4) > Orders.order_id
	# prods_id integer(4) >* Products.prod_id
	# prods_quantity integer(4)
	# order_price decimal(8,2)