from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from datetime import datetime
from ..models import order_details as model
from ..models import menu_items as menu_items_model
from ..schemas import orders as order_schema
from . import orders, resources, recipes

from sqlalchemy.exc import SQLAlchemyError
from . import resources, recipes


def create(db: Session, request):
    check_resources(db, request.menu_item_id, request.amount)

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
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)

        if "amount" in update_data:
            menu_item_id = db.query(model.OrderDetail).get(item_id).menu_item_id
            update_data["cost"] = get_cost(db, menu_item_id, update_data["amount"])
            check_resources(db, menu_item_id, update_data["amount"])
        if "menu_item_id" in update_data:
            amount = db.query(model.OrderDetail).get(item_id).amount
            update_data["cost"] = get_cost(db, update_data["menu_item_id"], amount)
            check_resources(db, update_data["menu_item_id"], amount)

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


def get_least_popular_dishes(db: Session):
    try:
        return db.query(model.OrderDetail).filter(model.OrderDetail.rating_score <= 3).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def get_most_popular_dishes(db: Session):
    try:
        return db.query(model.OrderDetail).filter(model.OrderDetail.rating_score >= 4).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def get_cost(db: Session, menu_item_id, amount):
    try:
        price = db.query(menu_items_model.MenuItem).get(menu_item_id).price
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return price*amount


def get_total_order_cost(db: Session, order_id):
    try:
        total_order_cost = 0.00
        
        all_order_details = read_all(db)
        for detail in all_order_details:
            if detail.order_id == order_id:
                total_order_cost += detail.cost
                
        discount_code = orders.get_discount(db, order_id)
        
        if discount_code: 
            total_order_cost *= (1 - discount_code)

        order_update_object = order_schema.OrderUpdate(
            total_cost=total_order_cost
        )

        orders.update(db, order_id, order_update_object)

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


def check_resources(db: Session, menu_item_id, amount):
    resource_ids = recipes.get_resource_ids(db, menu_item_id)
    resource_amounts = recipes.get_resource_amount_needed(db, menu_item_id, amount)

    resources.update_resources(db, resource_ids, resource_amounts)

