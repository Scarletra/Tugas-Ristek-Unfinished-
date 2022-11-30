from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

web = FastAPI() # Starter buat FastAPI

class Item(BaseModel): # Seralizer
    id: int # Semuanya bisa diganti sesuai kebutuhan
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode = True

# class Pengelolaan(BaseModel): Ini versi var yang nyambung sama dengan apa yang dibutuhin
#     nama_keluar: str
#     keterangan_keluar: str
#     jumlah_keluar: int
#     nama_masuk: str
#     keterangan_masuk: str
#     jumlah_masuk: int

#     class Config:
#         orm_mode = True

db = SessionLocal()

# @web.get('/')
# def index():
#     return {"msg": "Hello"}

# @web.get('/greet/{name}')
# def greet(name: str):
#     return {"greeting": f"Hello, {name}"}

# @web.get('/greet')
# def greet_optional_name(name:Optional[str]="player"):
#     return {"message": f"Hello {name}"}



# @web.put('/item/{item_id}')
# def update_item(item_id: int, item:Item):
#     return {'name':item.name,
#             'description':item.description,
#             'price':item.price,
#             'on_offer':item.on_offer
#             }


@web.get('/items', response_model=List[Item], status_code=200) # Ini kebawah penamaan var bisa diganti lagi
def get_all_items(): # Kurang lebih ini semua buat bikin kode CRUD (Create, Read, Update, Delete)
    items = db.query(models.Item).all()

    return items

@web.get('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

@web.post('/items', response_model=Item, 
        status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item):
    # db_item = db.quary(models.Item).filter(models.Item.name == item.name).first() Ini ga terlalu perlu karena cuma buat handle kalo item harus unique
    # if db_item is not None:
    #     raise HTTPException(status_code=400, detail="Item already exist")
    create_new = models.Item(
        name = item.name,
        price = item.price,
        description = item.description,
        on_offer = item.on_offer
    )

@web.get('/items', response_model=List[Pengelolaan], status_code=200) # Ini kebawah penamaan var bisa diganti lagi
def list_semua_aktivitas(): # Kurang lebih ini semua buat bikin kode CRUD (Create, Read, Update, Delete)
    items = db.query(models.Item).all()

    return items


    db.add(create_new)
    db.commit()

    return create_new

@web.put('/item/{item_id}', response_model=Item, status_code=status.HTTP_200_OK)
def update_an_item(item_id: int, item: Item):
    updated_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    updated_item.name = item.name
    updated_item.price = item.price
    updated_item.description = item.description
    updated_item.on_offer = item.on_offer

@web.delete('/item/{item_id}')
def delete_item(item_id: int):
    deleted_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if deleted_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

    return deleted_item
