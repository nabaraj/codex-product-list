# Product List API Instructions

This project contains a small FastAPI application that stores products in a static in-memory list. The app starts with five hard-coded products and supports listing, adding, modifying, and deleting products.

> Note: Products are stored in memory only. Any products added, modified, or deleted are reset when the server restarts.
This project contains a small FastAPI application that returns a hard-coded list of five products.

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
- `GET /products` returns the static list of five products.

## Try the API

Open the automatic Swagger UI documentation in a browser:

```text
http://127.0.0.1:8000/docs
```

Or request the product list with curl:

```bash
curl http://127.0.0.1:8000/products
```
