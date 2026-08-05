from fastapi import FastAPI
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool


PRODUCTS = [
    Product(
        id=1,
        name="Wireless Mouse",
        description="Ergonomic wireless mouse with USB receiver.",
        price=24.99,
        in_stock=True,
    ),
    Product(
        id=2,
        name="Mechanical Keyboard",
        description="Compact mechanical keyboard with blue switches.",
        price=79.99,
        in_stock=True,
    ),
    Product(
        id=3,
        name="USB-C Hub",
        description="Seven-in-one USB-C hub with HDMI and Ethernet.",
        price=49.99,
        in_stock=False,
    ),
    Product(
        id=4,
        name="Laptop Stand",
        description="Adjustable aluminum stand for laptops up to 17 inches.",
        price=34.99,
        in_stock=True,
    ),
    Product(
        id=5,
        name="Noise-Canceling Headphones",
        description="Over-ear Bluetooth headphones with active noise cancellation.",
        price=129.99,
        in_stock=True,
    ),
]

app = FastAPI(title="Product List API", version="1.0.0")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Product List API"}


@app.get("/products", response_model=list[Product])
def get_products() -> list[Product]:
    return PRODUCTS
