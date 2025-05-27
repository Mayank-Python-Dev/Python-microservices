from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import redis

app = FastAPI()

class Dominos(BaseModel):
    id : int
    name :  str
    description : str
    is_available : bool
    price : float

# Sample Domino's-style food items
dominos_food_items = [
    Dominos(id=1, name="Margherita", description="Classic cheese and tomato pizza", is_available=True, price=5.99),
    Dominos(id=2, name="Pepperoni Passion", description="Loaded with pepperoni & extra cheese", is_available=True, price=7.99),
    Dominos(id=3, name="Veggie Supreme", description="Packed with vegetables", is_available=True, price=6.99),
    Dominos(id=4, name="Chicken Dominator", description="Loaded with double chicken and cheese", is_available=False, price=8.49),
]

@app.get("/get_food_items")
def get_food_items():
    return {
        "status": 200,
        "data" : dominos_food_items
    }


@app.get("/get_food_item_price")
def get_food_item_price(name: Optional[str] = Query(None)):
    if name is None or not name:
        return {
            "status": 400,
            "message": "you have to pass the name!"
        }
    else:
        for i in dominos_food_items:
            if i.name.lower() == name.lower():
                return {
                    "status": 200,
                    "data" : i
                }
