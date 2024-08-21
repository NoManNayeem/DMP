from pydantic import BaseModel

class FirstPartyDataCreate(BaseModel):
    user_id: str
    data: str

    class Config:
        orm_mode = True

class SecondPartyDataCreate(BaseModel):
    partner_id: str
    data: str

    class Config:
        orm_mode = True

class ThirdPartyDataCreate(BaseModel):
    source: str
    data: str

    class Config:
        orm_mode = True
