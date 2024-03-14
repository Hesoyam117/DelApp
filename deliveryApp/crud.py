# app/crud.py

from sqlalchemy.orm import Session
from models.models import *# Client, Order
from schemas import *# ClientCreate, OrderCreate, ClientDelete

def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.client_id == client_id).first()
    if db_client:
        db.delete(db_client)
        db.commit()
        return True
    return False

def create_courier(db: Session, courier: CourierCreate):
    db_courier = Courier(**courier.dict())
    db.add(db_courier)
    db.commit()
    db.refresh(db_courier)
    return db_courier

def delete_courier(db: Session, courier_id: int):
    courier = db.query(Courier).filter(Courier.courier_id == courier_id).first()
    if courier:
        db.delete(courier)
        db.commit()
        return True
    return False

def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = Restaurant(**restaurant.dict())
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def delete_restaurant(db: Session, restaurant_id: int):
    db.query(Restaurant).filter(Restaurant.id == restaurant_id).delete()
    db.commit()

def create_order(db: Session, order: OrderCreate):
    db_order = Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def create_product(db: Session, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def create_order_detail(db: Session, order_detail: OrderDetailCreate):
    db_order_detail = OrderDetail(**order_detail.dict())
    db.add(db_order_detail)
    db.commit()
    db.refresh(db_order_detail)
    return db_order_detail

def delete_product(db: Session, product_id: int):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()

def delete_order_detail(db: Session, order_detail_id: int):
    db.query(OrderDetail).filter(OrderDetail.id == order_detail_id).delete()
    db.commit()

def get_clients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Client).offset(skip).limit(limit).all()

