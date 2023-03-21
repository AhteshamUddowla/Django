from django.db import models

# Create your models here.
class dress:
    id: int
    name: str
    image: str
    price: str
    offer: bool

class electronic:
    id: int
    name: str
    image: str
    price: int
    offer: bool
    offer_price: int

class jewellery:
    id: int
    name: str
    image: str
    price: int
    offer: bool
    offer_price: int


