# Product List API Instructions

This project contains a small FastAPI application that stores products in a static in-memory list. The app starts with five hard-coded products and supports listing, adding, modifying, and deleting products.

> Note: Products are stored in memory only. Any products added, modified, or deleted are reset when the server restarts.

## Prerequisites

- Python 3.10 or newer
- `pip`

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the API

Start the FastAPI server with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Endpoints

- `GET /` returns a welcome message.
- `GET /products` returns the static product list.
- `POST /products` adds a product to the list.
- `PUT /products/{product_id}` modifies an existing product.
- `DELETE /products/{product_id}` deletes an existing product.

## Swagger UI

Open the automatic Swagger UI documentation in a browser:

```text
http://127.0.0.1:8000/docs
```

## Curl Commands

### List products

```bash
curl http://127.0.0.1:8000/products
```

### Add a product

```bash
curl -X POST http://127.0.0.1:8000/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Webcam",
    "description": "1080p USB webcam with built-in microphone.",
    "price": 59.99,
    "in_stock": true
  }'
```

### Modify a product

```bash
curl -X PUT http://127.0.0.1:8000/products/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Wireless Mouse Pro",
    "description": "Ergonomic wireless mouse with programmable buttons.",
    "price": 29.99,
    "in_stock": true
  }'
```

### Delete a product

```bash
curl -X DELETE http://127.0.0.1:8000/products/1
```

## Postman Commands

Use these request settings in Postman after starting the server.

### List products

- Method: `GET`
- URL: `http://127.0.0.1:8000/products`
- Body: none

### Add a product

- Method: `POST`
- URL: `http://127.0.0.1:8000/products`
- Headers:
  - `Content-Type: application/json`
- Body type: `raw` JSON
- Body:

```json
{
  "name": "Webcam",
  "description": "1080p USB webcam with built-in microphone.",
  "price": 59.99,
  "in_stock": true
}
```

### Modify a product

- Method: `PUT`
- URL: `http://127.0.0.1:8000/products/1`
- Headers:
  - `Content-Type: application/json`
- Body type: `raw` JSON
- Body:

```json
{
  "name": "Wireless Mouse Pro",
  "description": "Ergonomic wireless mouse with programmable buttons.",
  "price": 29.99,
  "in_stock": true
}
```

### Delete a product

- Method: `DELETE`
- URL: `http://127.0.0.1:8000/products/1`
- Body: none
