from django.shortcuts import render, redirect
from . models import Product
from . forms import AddProduct
from django.http import HttpResponseRedirect


# home page
def index(request):
    cart = 0
    if request.method == 'POST':
        item = Product.objects.all()
        cart = cart
        return render(request, 'store/index.html', {'cart': cart, 'item': item, })
    else:
        item = Product.objects.all()
    return render(request, 'store/index.html', {'item': item, })


# about page
def about(request):
    return render(request, 'store/about.html', {})
# about page


# add product to detabase from site
def add_product(request):
    submitted = False
    if request.method == 'POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')
    else:
        form = AddProduct
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'store/add_product.html', {'form': form, 'submitted': submitted})


# show product
def show_product(request, product_id):
    item = Product.objects.get(pk=product_id)
    return render(request, 'store/show_product.html', {'item': item})


# Update product
def update_product(request, product_id):
    item = Product.objects.get(pk=product_id)
    form = AddProduct(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'store/update_product.html', {'form': form, 'item': item, })


def new_product(request):
    return render(request, 'store/new_product.html', {})
