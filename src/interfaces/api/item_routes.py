import os
from fastapi import APIRouter, HTTPException # type: ignore
from typing import List
from src.domain.models import ItemResponse, Item  # Ensure Item is imported
from src.application.item_service_impl import ItemServiceImpl
from src.infrastructure.repositories.item_repository_impl import ItemRepositoryImpl

router = APIRouter()

# Retrieve the connection string from the environment variable
connection_string = os.getenv("DATABASE_URL")

# Initialize the item service with the repository
item_service = ItemServiceImpl(repository=ItemRepositoryImpl())

@router.get("/items", response_model=List[ItemResponse], tags=["Items"], summary="Retrieve all items")
def get_items():
    """
    Retrieve a list of all items.
    """
    return item_service.get_all_items()

@router.get("/items/{item_id}", response_model=ItemResponse, tags=["Items"], summary="Retrieve an item by ID")
def get_item(item_id: int):
    """
    Retrieve a single item by its ID.
    """
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.post("/items", response_model=ItemResponse, tags=["Items"], summary="Create a new item")
def create_item(item: ItemResponse):  # Use ItemResponse for input validation
    """
    Create a new item with the given details.
    """
    # Convert ItemResponse to Item
    new_item = Item(id=None, name=item.name, description=item.description)  # Create an Item instance
    created_item = item_service.create_item(new_item)  # Pass the Item instance to the service
    return created_item

@router.put("/items/{item_id}", response_model=ItemResponse, tags=["Items"], summary="Update an existing item")
def update_item(item_id: int, item: ItemResponse):  # Use ItemResponse for input validation
    """
    Update an existing item with new details.
    """
    updated_item = item_service.update_item(item)  # Ensure the service method accepts the Pydantic model
    if updated_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated_item

@router.delete("/items/{item_id}", tags=["Items"], summary="Delete an item")
def delete_item(item_id: int):
    """
    Delete an item by its ID.
    """
    item_service.delete_item(item_id)
    return {"message": "Item deleted"}
