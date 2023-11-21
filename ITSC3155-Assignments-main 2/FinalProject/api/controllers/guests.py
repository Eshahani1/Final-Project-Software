from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import guests as model 
from sqlalchemy.exc import SQLAlchemyError


def create(db: Session, request):
    new_guest = model.Guest(
        name=request.name,
        phone_number=request.phone_number,
        address=request.address
    )

    try:
        db.add(new_guest)
        db.commit()
        db.refresh(new_guest)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_guest


def read_all(db: Session):
    try:
        result = db.query(model.Guest).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, guest_id):
    try:
        guest = db.query(model.Guest).filter(model.Guest.id == guest_id).first()
        if not guest:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return guest


def update(db: Session, guest_id, request):
    try:
        guest = db.query(model.Guest).filter(model.Guest.id == guest_id)
        if not guest.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        guest.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return guest.first()


def delete(db: Session, guest_id):
    try:
        guest = db.query(model.Guest).filter(model.Guest.id == guest_id)
        if not guest.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        guest.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
