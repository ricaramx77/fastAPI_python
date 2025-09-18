from fastapi import APIRouter
from models.product import Product
from typing import List

router = APIRouter(prefix="/products", tags=["products"])
products_db: List[Product] = []

@router.post("/", response_model=Product)
def create_product(product: Product):
    products_db.append(product)
    return product

@router.get("/", response_model=List[Product])
def list_products():
    return products_db
