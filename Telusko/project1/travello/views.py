from django.shortcuts import render
from . models import dress, electronic, jewellery

# Create your views here.
def index(request):
    dress1 = dress()
    dress1.name = "Man T-Shirt"
    dress1.price = 500
    dress1.image = "tshirt-img.png"
    dress1.offer = True
    dress1.offer_price = dress1.price-(dress1.price*.15)

    dress2 = dress()
    dress2.name = "Man Shirt"
    dress2.price = 600
    dress2.image = "dress-shirt-img.png"
    dress2.offer = False
    dress2.offer_price = dress2.price-(dress2.price*.15)

    dress3 = dress()
    dress3.name = "Women Scart"
    dress3.price = 700
    dress3.image = "women-clothes-img.png"
    dress3.offer = True
    dress3.offer_price = dress3.price-(dress3.price*.15)

    electronic1 = electronic()
    electronic1.name = "Laptop"
    electronic1.price = 500
    electronic1.image = "laptop-img.png"
    electronic1.offer = False
    electronic1.offer_price = electronic1.price-(electronic1.price*.15)

    electronic2 = electronic()
    electronic2.name = "Mobile"
    electronic2.price = 600
    electronic2.image = "mobile-img.png"
    electronic2.offer = True
    electronic2.offer_price = electronic2.price-(electronic2.price*.15)

    electronic3 = electronic()
    electronic3.name = "Computer"
    electronic3.price = 700
    electronic3.image = "computer-img.png"
    electronic3.offer = False
    electronic3.offer_price = electronic3.price-(electronic3.price*.15)

    jewellery1 = jewellery()
    jewellery1.name = "Jhumkas"
    jewellery1.price = 500
    jewellery1.image = "jhumka-img.png"
    jewellery1.offer = True
    jewellery1.offer_price = jewellery1.price-(jewellery1.price*.15)

    jewellery2 = jewellery()
    jewellery2.name = "Necklaces"
    jewellery2.price = 600
    jewellery2.image = "neklesh-img.png"
    jewellery2.offer = True
    jewellery2.offer_price = jewellery2.price-(jewellery2.price*.15)

    jewellery3 = jewellery()
    jewellery3.name = "Kangans"
    jewellery3.price = 700
    jewellery3.image = "kangan-img.png"
    jewellery3.offer = True
    jewellery3.offer_price = jewellery3.price-(jewellery3.price*.15)

    dresses = [dress1, dress2, dress3]
    electronics = [electronic1, electronic2, electronic3]
    jewelleries = [jewellery1, jewellery2, jewellery3]

    return render(request, 'index.html', {'dresses': dresses, 'electronics': electronics, 'jewelleries':jewelleries})
