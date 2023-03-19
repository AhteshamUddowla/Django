from django.shortcuts import render
from . models import dress, electronic, jewellery

# Create your views here.
def index(request):
    dress1 = dress()
    dress1.name = "Man T-Shirt"
    dress1.price = "500"
    dress1.image = "tshirt-img.png"

    dress2 = dress()
    dress2.name = "Man Shirt"
    dress2.price = "600"
    dress2.image = "dress-shirt-img.png"

    dress3 = dress()
    dress3.name = "Women Scart"
    dress3.price = "700"
    dress3.image = "women-clothes-img.png"

    electronic1 = electronic()
    electronic1.name = "Laptop"
    electronic1.price = "500"
    electronic1.image = "laptop-img.png"

    electronic2 = electronic()
    electronic2.name = "Mobile"
    electronic2.price = "600"
    electronic2.image = "mobile-img.png"

    electronic3 = electronic()
    electronic3.name = "Computer"
    electronic3.price = "700"
    electronic3.image = "computer-img.png"

    jewellery1 = jewellery()
    jewellery1.name = "Jhumkas"
    jewellery1.price = "500"
    jewellery1.image = "jhumka-img.png"

    jewellery2 = jewellery()
    jewellery2.name = "Necklaces"
    jewellery2.price = "600"
    jewellery2.image = "neklesh-img.png"

    jewellery3 = jewellery()
    jewellery3.name = "Kangans"
    jewellery3.price = "700"
    jewellery3.image = "kangan-img.png"

    dresses = [dress1, dress2, dress3]
    electronics = [electronic1, electronic2, electronic3]
    jewelleries = [jewellery1, jewellery2, jewellery3]

    return render(request, 'index.html', {'dresses': dresses, 'electronics': electronics, 'jewelleries':jewelleries})
