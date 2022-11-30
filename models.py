from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text

class Item(Base): # Define class. NB : Bisa dimodif diganti nama yang lebih sesuai sama permintaan
    __tablename__ = "items"
    id = Column(Integer) # Ini cuma contoh, tinggal diganti sama var yang diperluin buat database web nya
    name = Column(String(255), nullable=False) # Nullable means cant be empty data
    description = Column(Text, nullable=False) # Ex param dari string adalah max character
    price = Column(Integer, nullable=False)
    on_offer = Column(Boolean, default=False) # Default bisa beda - beda tetapi jika tidak dedefine akan set value nya false untuk dicontoh


    def __repr__(self):
        return f"<Item name = {self.name} price = {self.price}"

class Pengelolaan(Base): # Define class. NB : Bisa dimodif diganti nama yang lebih sesuai sama permintaan
    __tablename__ = "cycle_duit"
    nama_keluar = Column(Text, nullable=False) # Ini cuma contoh, tinggal diganti sama var yang diperluin buat database web nya
    keterangan_keluar = Column(Text, nullable=False) # Nullable means cant be empty data
    jumlah_keluar = Column(Integer, nullable=False) # Ex param dari string adalah max character
    nama_masuk = Column(Text, nullable=False)
    keterangan_masuk = Column(Text, nullable=False)
    jumlah_masuk = Column(Integer, nullable=False) # Default bisa beda - beda tetapi jika tidak dedefine akan set value nya false untuk dicontoh


    def __repr__(self):
        return f"<Item name = {self.name} price = {self.price}"