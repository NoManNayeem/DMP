from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import database, models
from ..schemas.data_schemas import FirstPartyDataCreate, SecondPartyDataCreate, ThirdPartyDataCreate
from ..auth import get_current_user

router = APIRouter(
    prefix="/data",
    tags=["Data Collection"]
)



# First-Party Data Endpoints
@router.post("/first-party/", response_model=FirstPartyDataCreate)
def create_first_party_data(data: FirstPartyDataCreate, db: Session = Depends(database.get_db)):
    db_data = models.FirstPartyData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/first-party/", response_model=List[FirstPartyDataCreate])
def get_all_first_party_data(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.FirstPartyData).all()

@router.get("/first-party/{id}", response_model=FirstPartyDataCreate)
def get_first_party_data(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    data = db.query(models.FirstPartyData).filter(models.FirstPartyData.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.put("/first-party/{id}", response_model=FirstPartyDataCreate)
def update_first_party_data(id: int, data: FirstPartyDataCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_data = db.query(models.FirstPartyData).filter(models.FirstPartyData.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    for key, value in data.dict().items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.delete("/first-party/{id}", response_model=FirstPartyDataCreate)
def delete_first_party_data(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_data = db.query(models.FirstPartyData).filter(models.FirstPartyData.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db.delete(db_data)
    db.commit()
    return db_data

# Second-Party Data Endpoints
@router.post("/second-party/", response_model=SecondPartyDataCreate)
def create_second_party_data(data: SecondPartyDataCreate, db: Session = Depends(database.get_db)):
    db_data = models.SecondPartyData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/second-party/", response_model=List[SecondPartyDataCreate])
def get_all_second_party_data(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.SecondPartyData).all()

@router.get("/second-party/{id}", response_model=SecondPartyDataCreate)
def get_second_party_data(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    data = db.query(models.SecondPartyData).filter(models.SecondPartyData.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.put("/second-party/{id}", response_model=SecondPartyDataCreate)
def update_second_party_data(id: int, data: SecondPartyDataCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_data = db.query(models.SecondPartyData).filter(models.SecondPartyData.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    for key, value in data.dict().items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.delete("/second-party/{id}", response_model=SecondPartyDataCreate)
def delete_second_party_data(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_data = db.query(models.SecondPartyData).filter(models.SecondPartyData.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db.delete(db_data)
    db.commit()
    return db_data

# Third-Party Data Endpoints
@router.post("/third-party/", response_model=ThirdPartyDataCreate)
def create_third_party_data(data: ThirdPartyDataCreate, db: Session = Depends(database.get_db)):
    db_data = models.ThirdPartyData(**data.dict())
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.get("/third-party/", response_model=List[ThirdPartyDataCreate])
def get_all_third_party_data(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.ThirdPartyData).all()

@router.get("/third-party/{id}", response_model=ThirdPartyDataCreate)
def get_third_party_data(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    data = db.query(models.ThirdPartyData).filter(models.ThirdPartyData.id == id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@router.put("/third-party/{id}", response_model=ThirdPartyDataCreate)
def update_third_party_data(id: int, data: ThirdPartyDataCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_data = db.query(models.ThirdPartyData).filter(models.ThirdPartyData.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    for key, value in data.dict().items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

@router.delete("/third-party/{id}", response_model=ThirdPartyDataCreate)
def delete_third_party_data(id: int, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    db_data = db.query(models.ThirdPartyData).filter(models.ThirdPartyData.id == id).first()
    if db_data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    db.delete(db_data)
    db.commit()
    return db_data
