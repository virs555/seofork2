from typing import Union

from fastapi import FastAPI
from models import Item

app = FastAPI()


@app.get("/yandex")
def get_yandex_results():
    return {"Hello": "World"}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}