# app/schemas.py
from typing import List, Optional, Union
from datetime import datetime
from pydantic import BaseModel

class ClientBase(BaseModel):
    client_id: int
    name: str
    address: str
    phone: str

class ClientCreate(ClientBase):
    pass

class ClientDelete(BaseModel):
    client_id: int
  
class CourierBase(BaseModel):
    courier_id: int
    client_id: int
    name: str
    phone_number: str
    rating: int
    status: str
    order_id: Optional[Union[int, None]]
    geolocation: int

class CourierCreate(CourierBase):
    pass

class CourierDelete(CourierBase):
    pass    

class RestaurantCreate(BaseModel):
    rest_id: int
    name: str
    address: str
    type: str
    phone_number: str
    working_time: str

class RestaurantDelete(BaseModel):
    restaurant_id: int

class OrderBase(BaseModel):
    order_id: int
    client_id: int
    courier_id: int
    rest_id: int
    status: str
    date: datetime
    pass


class OrderCreate(OrderBase):
    pass

class ProductCreate(BaseModel):
    prod_id: int
    rest_id: int
    name: str
    price: float
    description: str
    category: str

class OrderDetailCreate(BaseModel):
    order_det_id: int
    order_id: int
    comment: str