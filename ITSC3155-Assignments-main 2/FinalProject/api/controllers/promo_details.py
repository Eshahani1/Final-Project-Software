from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import promo_details as model
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
<<<<<<< HEAD:ITSC3155-Assignments-main 2/FinalProject/api/controllers/menu.py
    new_item = model.Menu(
        id=request.id,
        item_name=request.item_name,
        price=request.price,
        calories=request.calories
||||||| 69af943:ITSC3155-Assignments-main 2/FinalProject/api/controllers/menu.py
    new_item = model.Menu(
        menu_id=request.menu_id,
        resource_id=request.resource_id,
        amount=request.amount
=======
    new_item = model.PromoDetail(
        promo_id=request.promo_id,
        guest_id=request.guest_id
>>>>>>> database-alteration:ITSC3155-Assignments-main 2/FinalProject/api/controllers/promo_details.py
    )

    try:
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.PromoDetail).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.PromoDetail).filter(model.PromoDetail.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.PromoDetail).filter(model.PromoDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.PromoDetail).filter(model.PromoDetail.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
