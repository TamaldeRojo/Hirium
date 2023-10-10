from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime
from constants.userRoles import UserRoles 
from models.pyObjectId import PyObjectId
from bson import ObjectId

class User(BaseModel): 
    #userId: Optional[str] = None
    name: str # = Field(default = None)
    email: EmailStr # = Field(default = None)
    password: str # = Field(default = None)
    role: UserRoles
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    
    class Config:
        from_attributes = True
        allow_population_by_name = True
        json_encoders = {ObjectId: str}
        
class UserSingIn(BaseModel): 
    email: EmailStr # = Field(default = None)
    password: str # = Field(default = None)
    
    
        
       