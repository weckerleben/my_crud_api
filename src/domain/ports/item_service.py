from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Item

class ItemService(ABC):
    @abstractmethod
    def get_all_items(self) -> List[Item]:
        pass

    @abstractmethod
    def get_item(self, item_id: int) -> Item:
        pass

    @abstractmethod
    def create_item(self, item: Item) -> Item:
        pass

    @abstractmethod
    def update_item(self, item: Item) -> Item:
        pass

    @abstractmethod
    def delete_item(self, item_id: int) -> None:
        pass
