from typing import List
from src.domain.models import Item
from src.domain.ports.item_service import ItemService
from src.domain.ports.item_repository import ItemRepository

class ItemServiceImpl(ItemService):
    def __init__(self, repository: ItemRepository):
        self.repository = repository

    def get_all_items(self) -> List[Item]:
        return self.repository.get_all()

    def get_item(self, item_id: int) -> Item:
        return self.repository.get_by_id(item_id)

    def create_item(self, item: Item) -> Item:
        return self.repository.create(item)

    def update_item(self, item: Item) -> Item:
        return self.repository.update(item)

    def delete_item(self, item_id: int) -> None:
        self.repository.delete(item_id)
