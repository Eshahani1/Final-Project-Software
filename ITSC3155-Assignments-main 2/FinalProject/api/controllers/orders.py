from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from datetime import datetime
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
from ..models import promos as promo_model


def create(db: Session, request):
    current_date = datetime.now()

    try:
        new_order = model.Order(
            guest_id=request.guest_id,
            promo_code=request.promo_code,
            tracking_nums=request.tracking_nums,
            order_status=request.order_status,
            card_number=request.card_number,
            pin=request.pin,
            method=request.method,
            transaction_status=request.transaction_status,
            order_preference=request.order_preference,
            total_cost=0.00
        )

        if request.promo_code:
            promo = db.query(promo_model.Promo).filter(promo_model.Promo.code == request.promo_code).first()
            if promo:
                if promo.expiration_date and promo.expiration_date < current_date:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promo code has expired")

                new_order.discount_code = promo.discount
                
        db.add(new_order)
        db.commit()
        db.refresh(new_order)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_order


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, order_id):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order


def update(db: Session, order_id, request):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)

        if "promo_code" in update_data:
            promo = db.query(promo_model.Promo).filter(promo_model.Promo.code == request.promo_code).first()
            if promo:
                if promo.expiration_date and promo.expiration_date < current_date:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Promo code has expired")

                new_order.discount_code = promo.discount

        order.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order.first()


def delete(db: Session, order_id):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        order.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def read_order_from_tracking_number(db: Session, tracking_number: int):
    try:
        order = db.query(model.Order).filter(model.Order.tracking_nums == tracking_number).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tracking number not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order


def get_orders_between_dates(db: Session, start_date: datetime, end_date: datetime):
   return db.query(model.Order).filter(model.Order.order_date >= start_date, model.Order.order_date <= end_date).all()


def get_discount_code(db: Session, order_id):
    try:
        order = db.query(model.Order).filter(model.Order.id == order_id).first()
        if order:
            return order.discount_code
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    
    
def get_revenue_between_dates(db: Session, start_date: datetime, end_date: datetime):
    orders = get_orders_between_dates(db, start_date, end_date)
    revenue = 0.00
    for order in orders:
        revenue += order.total_cost
    return revenue
        
    