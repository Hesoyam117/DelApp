from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text, MetaData, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel
from sqlalchemy import DECIMAL as Decimal

Base = declarative_base()

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
