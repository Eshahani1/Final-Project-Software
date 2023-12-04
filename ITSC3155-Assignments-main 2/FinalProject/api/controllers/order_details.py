from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import order_details as model
from ..models import menu_items as menu_items
from . import orders as update_cost
from ..schemas import orders as order
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_item = model.OrderDetail(
        order_id=request.order_id,
        menu_item_id=request.menu_item_id,
        amount=request.amount,
        rating_score=request.rating_score,
        rating_review=request.rating_review,
        cost=get_cost(db, request.menu_item_id, request.amount)
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    get_total_order_cost(db, request.order_id)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.OrderDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Detail Id not found!")
        update_data = request.dict(exclude_unset=True)

        if "amount" in update_data:
            update_data["cost"] = get_cost(db,
                                           db.query(model.OrderDetail).get(item_id).menu_item_id,
                                           update_data["amount"])
        if "menu_item_id" in update_data:
            update_data["cost"] = get_cost(db,
                                           update_data["menu_item_id"],
                                           db.query(model.OrderDetail).get(menu_item_id).amount)

        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    get_total_order_cost(db, db.query(model.OrderDetail).get(item_id).order_id)
    
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.OrderDetail).filter(model.OrderDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def get_cost(db: Session, menu_item_id, amount):
    try:
        price = db.query(menu_items.MenuItem).get(menu_item_id).price   
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return price*amount


def get_total_order_cost(db: Session, order_id):
    total_order_cost = 0.00
    all_order_details = read_all(db)
    for detail in all_order_details:
        if detail.order_id == order_id:
            total_order_cost += detail.cost
    order_update_object = order.OrderUpdate(
        total_cost=total_order_cost
    )
    update_cost.update(db, order_id, order_update_object)
