from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    in_stock: bool


class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool


class ProductUpdate(BaseModel):
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


def find_product_index(product_id: int) -> int:
    for index, product in enumerate(PRODUCTS):
        if product.id == product_id:
            return index
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with id {product_id} was not found.",
    )


def get_next_product_id() -> int:
    if not PRODUCTS:
        return 1
    return max(product.id for product in PRODUCTS) + 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the Product List API"}


@app.get("/products", response_model=list[Product])
def get_products() -> list[Product]:
    return PRODUCTS


@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(product: ProductCreate) -> Product:
    new_product = Product(id=get_next_product_id(), **product.dict())
    PRODUCTS.append(new_product)
    return new_product


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate) -> Product:
    product_index = find_product_index(product_id)
    updated_product = Product(id=product_id, **product.dict())
    PRODUCTS[product_index] = updated_product
    return updated_product


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int) -> None:
    product_index = find_product_index(product_id)
    PRODUCTS.pop(product_index)
