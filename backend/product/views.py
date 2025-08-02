from django.shortcuts import render
from .models import Product,Tag,Category

# Create your views here.
def product(request):
    products=Product.objects.all().order_by('-created_day')
    products=products.filter(public=True)
    return render(request,'product/product_base.html',{'products':products})