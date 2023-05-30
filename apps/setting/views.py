from django.shortcuts import render
from apps.setting.models import Setting
from apps.products.models import Products
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    products = Products.objects.all()
    context = {
        'setting': setting,
        'products':products,
    }
    return render(request,'index.html', context)    