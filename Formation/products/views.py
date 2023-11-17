from django.shortcuts import render
from .models import products
from .form import ProductForm

def products_list(request, *args, **kwargs):
     product = products.objects.all()
     context = {
      'produts': product
     }
     return render (request,'products/detail.html', context )

# def productCreate(request):
#      form = ProductForm (request.POST or None)
#      if form.is_valid():
#           form.save()
#           form = ProductForm()
#           mes = "we have receive your message"
          
#      return render(request, 'products/create.html', {'form':form, 'message':mes})

def productCreate(request):
     return render(request, 'products/create.html')