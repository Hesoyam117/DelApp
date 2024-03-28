from decimal import Decimal
import uuid
from typing import Optional
from pydantic import BaseModel
from fastapi_users import schemas

###############################################################################################################
#Авторизация
class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    role_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
    role_id: int
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
###############################################################################################################
#Клиенты
class ClientBase(BaseModel):
              
    client_id: int
    name: str
    address: Optional[str] = None
    phone: Optional[str] = None

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    client_id: int

    class Config:
        orm_mode = True
###############################################################################################################
class CourierBase(BaseModel):
    courier_id: int
    client_id: Optional[int] = None
    name: str
    phone_number: Optional[str] = None
    rating: Optional[int] = None
    status: str
    order_id: Optional[int]
    geolocation: int

class CourierCreate(CourierBase):
    pass

class Courier(CourierBase):
    client_id: int

    class Config:
        orm_mode = True
###############################################################################################################
#Рестораны
class RestaurantBase(BaseModel):
    rest_id: int
    name: str
    address: str
    type: str     
    phone_number: Optional[str] = None
    working_time: str

class RestaurantCreate(RestaurantBase):
    pass

class Restaurant(RestaurantBase):
    rest_id: int

    class Config:
        orm_mode = True
###############################################################################################################
#Продукты
class ProductBase(BaseModel):
    prod_id: int
    rest_id: int
    name: str
    price: int
    description: str
    category: str     


class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    rest_id: int

    class Config:
        orm_mode = True
###############################################################################################################
#Заказы
class OrderBase(BaseModel):
    order_id: int
    client_id: int
    courier_id: int
    rest_id: int
    status: str
    date: str     


class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    rest_id: int

    class Config:
        orm_mode = True