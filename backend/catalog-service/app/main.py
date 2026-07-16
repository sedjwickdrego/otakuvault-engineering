from fastapi import FastAPI

from .products import products

app = FastAPI(
    title="OtakuVault Catalog Service",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "service": "catalog-service",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/products")
def get_products():
    return products