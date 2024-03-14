# app/api/router.py
from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *# ClientCreate, OrderCreate
from crud import *# create_client, create_order, get_clients
from database import SessionLocal
from fastapi.middleware.cors import CORSMiddleware
from router import router as api_router

router = APIRouter()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post("/clients/")
# def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
#     return create_client(db, client)

# @router.delete("/clients/{client_id}")
# def delete_client_endpoint(client_id: int, db: Session = Depends(get_db)):
#     success = delete_client(db, client_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Client not found")
#     return {"message": "Client deleted successfully"}

# @router.post("/orders/")
# def create_new_order(order: OrderCreate, db: Session = Depends(get_db)):
#     return create_order(db, order)

# @router.get("/clients/")
# def read_clients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return get_clients(db, skip=skip, limit=limit)
