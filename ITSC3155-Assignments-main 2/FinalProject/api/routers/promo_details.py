from fastapi import APIRouter, Depends, FastAPI, status, Response
from sqlalchemy.orm import Session
from ..controllers import promo_details as controller
from ..schemas import promo_details as schema
from ..dependencies.database import engine, get_db

router = APIRouter(
    tags=['Promo Details'],
    prefix="/promodetails"
)


@router.post("/", response_model=schema.PromoDetail)
def create(request: schema.PromoDetailCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)


@router.get("/", response_model=list[schema.PromoDetail])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)


@router.get("/{item_id}", response_model=schema.PromoDetail)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)


@router.put("/{item_id}", response_model=schema.PromoDetail)
def update(item_id: int, request: schema.PromoDetailUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)


@router.delete("/{item_id}")
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
