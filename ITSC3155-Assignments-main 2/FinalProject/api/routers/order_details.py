from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from datetime import datetime
from typing import List
from ..controllers import order_details as controller
from ..schemas import order_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Order Details'],
    prefix="/orderdetails"
)


@router.post("/", response_model=schema.OrderDetail)
def create(request: schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.OrderDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.OrderDetail)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.OrderDetail)
def update(item_id: int, request: schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)


@router.get("/least_popular_dishes/")
def get_least_popular_dishes(db: Session = Depends(get_db)):
    return controller.get_least_popular_dishes(db)


@router.get("/most_popular_dishes/", response_model=List[schema.OrderDetail])
def get_most_popular_dishes(db: Session = Depends(get_db)):
    return controller.get_most_popular_dishes(db)
