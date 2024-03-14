# app/api/router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *#ClientCreate, OrderCreate, ClientDelete
from crud import *#create_client, create_order, get_clients, delete_client
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/clients/")
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.delete("/clients/{client_id}")
def delete_client_endpoint(client_id: int, db: Session = Depends(get_db)):
    success = delete_client(db, client_id)
    if not success:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}

@router.post("/couriers/")
def create_new_courier(courier: CourierCreate, db: Session = Depends(get_db)):
    return create_courier(db, courier)

@router.delete("/couriers/{courier_id}")
def delete_courier_endpoint(courier_id: int, db: Session = Depends(get_db)):
    success = delete_courier(db, courier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Courier not found")
    return {"message": "Courier deleted successfully"}

@router.post("/restaurants/")
def create_new_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return create_restaurant(db, restaurant)

@router.delete("/restaurants/{restaurant_id}")
def delete_restaurant_endpoint(restaurant_id: int, db: Session = Depends(get_db)):
    delete_restaurant(db, restaurant_id)
    return {"message": "Restaurant deleted successfully"}

@router.post("/orders/")
def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.post("/products/")
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.post("/order-details/")
def create_new_order_detail(order_detail: OrderDetailCreate, db: Session = Depends(get_db)):
    return create_order_detail(db, order_detail)

@router.delete("/products/{product_id}")
def delete_product_endpoint(product_id: int, db: Session = Depends(get_db)):
    delete_product(db, product_id)
    return {"message": "Product deleted successfully"}

@router.delete("/order-details/{order_detail_id}")
def delete_order_detail_endpoint(order_detail_id: int, db: Session = Depends(get_db)):
    delete_order_detail(db, order_detail_id)
    return {"message": "Order Detail deleted successfully"}

@router.get("/clients/")
def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_clients(db, skip=skip, limit=limit)
