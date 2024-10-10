from sqlalchemy.orm import Session
from typing import List
from src.domain.models import Item
from src.domain.ports.item_repository import ItemRepository
from src.infrastructure.database import SessionLocal

class ItemRepositoryImpl(ItemRepository):
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self) -> List[Item]:
        return self.db.query(Item).all()

    def get_by_id(self, item_id: int) -> Item:
        return self.db.query(Item).filter(Item.id == item_id).first()

    def create(self, item: Item) -> Item:
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def update(self, item: Item) -> Item:
        db_item = self.get_by_id(item.id)
        if db_item:
            db_item.name = item.name
            db_item.description = item.description
            self.db.commit()
            self.db.refresh(db_item)
        return db_item

    def delete(self, item_id: int) -> None:
        db_item = self.get_by_id(item_id)
        if db_item:
            self.db.delete(db_item)
            self.db.commit()
