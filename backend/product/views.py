from django.shortcuts import render
from .models import Product,Tag,Category

# Create your views here.
def product(request):
    products=Product.objects.all()
    return render(request,'product/product_base.html',{'products':products})