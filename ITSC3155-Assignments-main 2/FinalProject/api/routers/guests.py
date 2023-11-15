from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import guests as controller
from ..schemas import guests as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Guests'],
    prefix="/guests"
)


@router.post("/", response_model=schema.Guest)
def create(request: schema.GuestCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.Guest])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{guest_id}", response_model=schema.Guest)
def read_one(guest_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, guest_id=guest_id)


@router.put("/{guest_id}", response_model=schema.Guest)
def update(guest_id: int, request: schema.GuestUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, guest_id=guest_id)


@router.delete("/{guest_id}")
def delete(guest_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, guest_id=guest_id)
