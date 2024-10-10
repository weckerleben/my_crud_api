from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'  # Define the table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)

# Pydantic model for response validation
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        from_attributes = True  # Use 'from_attributes' instead of 'orm_mode' for Pydantic v2
