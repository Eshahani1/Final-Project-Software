from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from datetime import datetime
from ..controllers import orders as controller
from ..schemas import orders as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Orders'],
    prefix="/orders"
)


@router.post("/", response_model=schema.Order)
def create(request: schema.OrderCreate, db: Session = Depends(get_db)):
    print("aa")
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Order])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{order_id}", response_model=schema.Order)
def read_one(order_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, order_id=order_id)


@router.put("/{order_id}", response_model=schema.Order)
def update(order_id: int, request: schema.OrderUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, order_id=order_id)


@router.delete("/{order_id}")
def delete(order_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, order_id=order_id)


@router.get("/tracking_nums/{tracking_number}", response_model=schema.Order)
def read_order_from_tracking_number(tracking_number: int, db: Session = Depends(get_db)):
    return controller.read_order_from_tracking_number(db, tracking_number=tracking_number)


@router.get("/orders-by-date/", response_model=list[schema.Order])
def read_orders_between_dates(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return controller.get_orders_between_dates(db, start_date, end_date)


@router.get("/revenue-by-date/", response_model=float)
def read_revenue_between_dates(start_date: datetime, end_date: datetime, db: Session = Depends(get_db)):
    return controller.get_revenue_between_dates(db, start_date, end_date)
