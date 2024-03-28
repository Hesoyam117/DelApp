from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from auth import schemas
from auth import database
from models import models
router = APIRouter()


# Эндпоинт для создания клиента
# @router.post("/clients/", response_model=schemas.Client)
# async def create_client(client: schemas.ClientCreate, db: AsyncSession = Depends(database.get_async_session)):
#     async with db() as session:
#         db_client = database.Client(**client.dict())
#         session.add(db_client)
#         await session.commit()
#         return db_client
###############################################################################################################
#Клиенты
@router.post("/clients/", response_model=schemas.Client)
async def create_client(client: schemas.ClientCreate, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        db_client = models.Client(**client.dict())
        session.add(db_client)
        await session.commit()  
        return db_client


# Эндпоинт для получения клиента по его ID
@router.get("/clients/{client_id}", response_model=schemas.Client)
async def get_client(client_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        client = await session.get(models.Client, client_id)
        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        return client


# Эндпоинт для удаления клиента по его ID
@router.delete("/clients/{client_id}")
async def delete_client(client_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        client = await session.get(models.Client, client_id)
        if client is None:
            raise HTTPException(status_code=404, detail="Client not found")
        await session.delete(client)
        await session.commit()
        return {"message": "Client deleted successfully"}

###############################################################################################################
#Курьеры
@router.post("/couriers/", response_model=schemas.Courier)
async def create_courier(courier: schemas.CourierCreate, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        db_courier = models.Courier(**courier.dict())
        session.add(db_courier)
        await session.commit()  
        return db_courier

# Эндпоинт для получения курьера по его ID
@router.get("/couriers/{courier_id}", response_model=schemas.Courier)
async def get_courier(courier_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        courier = await session.get(models.Courier, courier_id)
        if courier is None:
            raise HTTPException(status_code=404, detail="Courier not found")
        return courier


# Эндпоинт для удаления Курьера по его ID
@router.delete("/couriers/{courier_id}")
async def delete_courier(courier_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        courier = await session.get(models.Courier, courier_id)
        if courier is None:
            raise HTTPException(status_code=404, detail="Courier not found")
        await session.delete(courier)
        await session.commit()
        return {"message": "Courier deleted successfully"}
###############################################################################################################
#Рестораны
@router.post("/restaurants/", response_model=schemas.Restaurant)
async def create_restaurant(restaurant: schemas.RestaurantCreate, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        db_restaurant = models.Restaurant(**restaurant.dict())
        session.add(db_restaurant)
        await session.commit()  
        return db_restaurant

# Эндпоинт для получения ресторана по его ID
@router.get("/restaurants/{restaurant_id}", response_model=schemas.Restaurant)
async def get_restaurantt(restaurant_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        restaurant = await session.get(models.Restaurant, restaurant_id)
        if restaurant is None:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        return restaurant


# Эндпоинт для удаления ресторана по его ID
@router.delete("/restaurants/{restaurant_id}")
async def delete_restaurant(restaurant_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        restaurant = await session.get(models.Restaurant, restaurant_id)
        if restaurant is None:
            raise HTTPException(status_code=404, detail="Restaurant not found")
        await session.delete(restaurant)
        await session.commit()
        return {"message": "Restaurant deleted successfully"}
###############################################################################################################
#Продукты
@router.post("/products/", response_model=schemas.Product)
async def create_product(product: schemas.ProductCreate, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        db_product = models.Product(**product.dict())
        session.add(db_product)
        await session.commit()  
        return db_product

# Эндпоинт для получения продукта по его ID
@router.get("/products/{product_id}", response_model=schemas.Product)
async def get_product(product_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        product = await session.get(models.Product, product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return product

# Эндпоинт для удаления продукта по его ID
@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        product = await session.get(models.Product, product_id)
        if product is None:
            raise HTTPException(status_code=404, detail="Product not found")
        await session.delete(product)
        await session.commit()
        return {"message": "Product deleted successfully"}
###############################################################################################################
#Заказы
@router.post("/orders/", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        db_order = models.Order(**order.dict())
        session.add(db_order)
        await session.commit()  
        return db_order

# Эндпоинт для получения заказа по его ID
@router.get("/orders/{order_id}", response_model=schemas.Order)
async def get_order(order_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        order = await session.get(models.Order, order_id)
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return order

# Эндпоинт для удаления заказа по его ID
@router.delete("/orders/{order_id}")
async def delete_order(order_id: int, db: AsyncSession = Depends(database.get_async_session)):
    async with db as session:
        order = await session.get(models.Order, order_id)
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        await session.delete(order)
        await session.commit()
        return {"message": "Order deleted successfully"}
