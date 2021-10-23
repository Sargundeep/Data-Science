from fastapi import FastAPI,Path,Query,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

# @app.get("/")
# def home():
#     return{"Data":"Test"}

# @app.get("/about")
# def about():
#     return{"Data":"About"}
class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None

class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None


# inventory = {
#     1: {
#         "name":"Milk",
#         "price":3.99,
#         "brand":"Regular"
#     }
# }

inventory = {}


#===============================================GET ITEM========================================
# @app.get("/get-item/{item_id}")
# def get_item(item_id: int = Path(None,description="The ID of the item u like to view ",gt=0,lt=2)):  gt and lt --->greater than less than condition
#     return inventory[item_id]

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(None,description="The ID of the item u would like to view ",gt=0)):
    return inventory[item_id]




# @app.get("/get-by-name/{item-id}")
# def get_item( *, item_id:int, test: int,name:Optional[str] = None):
#     for item_id in inventory:
#         if inventory[item_id]["name"] == name:
#             return inventory[item_id]
#     return {"Data":"Not found"}

@app.get("/get-by-name/{item-id}")
def get_item( name:str = Query(None,description="The name of the item u would like to view ",max_length=10,min_length=2)):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    # return {"Data":"Not found"} without using HTTPException 
    raise HTTPException(status_code = 404 , detail="Item name not found")


#==============================================CREATE ITEM=================================================

# @app.post("/create-item/{item_id}")
# def create_item(item_id:int,item:Item):
#     if item_id in inventory:
#         return {"Error": "Item ID already exists. "}
    
#     inventory[item_id] = {"name":item.name,"brand":item.brand,"price":item.price}
#     return inventory[item_id]

@app.post("/create-item/{item_id}")
def create_item(item_id:int,item:Item):
    if item_id in inventory:
        # return {"Error": "Item ID already exists. "}
        raise HTTPException(status_code = 400 , detail="Item already exists")
    inventory[item_id] = item #fast api will convert the item object into jason
    return inventory[item_id]

#=======================================UPDATE ITEM==============================================
# @app.put("/update-item/{item_id}")
# def update_item(item_id: int,item:Item):
#     if item_id not in inventory:
#         return {"Error":"Item iD doen't exists"}

#     inventory[item_id] = item
#     return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int,item:UpdateItem):
    if item_id not in inventory:
        # return {"Error":"Item iD doen't exists"}
        raise HTTPException(status_code = 404 , detail="Item ID doesn't exists")
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The ID of the item to be deleted:")):
    if item_id not in inventory:
        # return {"Error" : " ID doen't exists"}
        raise HTTPException(status_code = 404 , detail="Item ID doesn't exists")
    del inventory[item_id]
    return {"Success":"Item deleted!"}












