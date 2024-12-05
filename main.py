from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
def read_root():
    return {"message": "Hello swagger World"}

@app.post("/items/")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0",port=8000)
    