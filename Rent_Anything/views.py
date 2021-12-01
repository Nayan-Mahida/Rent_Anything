from django.shortcuts import render, redirect
from .forms import itemsForm, UserCrationForm, AuthForm
from django.contrib.auth import login, logout
from .models import items

# CRUD Operations: Create, Retrieve, Update, Delete


def view_products(request):
    # Retrieve all the products and render products.html with the data
    products = items.objects.all()
    context = {'products': products}
    return render(request, 'Rent_Anthing/items.html', context)


def create_product(request):
    # Create a form instance and populate it with data from the request
    form = itemsForm(request.POST or None)
    # check whether it's valid:
    if form.is_valid():
        # save the record into the db
        form.save()
        # after saving redirect to view_product page
        return redirect('view_products')

    # if the request does not have post data, a blank form will be rendered
    return render(request, 'Rent_Anthing/product-form.html', {'form': form})


def update_product(request, id):
    # Get the product based on its id
    product = items.objects.get(id=id)
    # populate a form instance with data from the data on the database
    # instance=product allows to update the record rather than creating a new record when save method is called
    form = itemsForm(request.POST or None, instance=product)

    # check whether it's valid:
    if form.is_valid():
        # update the record in the db
        form.save()
        # after updating redirect to view_product page
        return redirect('view_products')

    # if the request does not have post data, render the page with the form containing the product's info
    return render(request, 'Rent_Anthing/product-form.html', {'form': form})


def delete_product(request, id):
    # Get the product based on its id
    product = items.objects.get(id=id)

    # if this is a POST request, we need to delete the form data
    if request.method == 'POST':
        product.delete()
        # after deleting redirect to view_product page
        return redirect('view_products')

    # if the request is not post, render the page with the product's info
    return render(request, 'Rent_Anthing/delete-confirm.html', {'product': product})

def register_user(request):
    form = UserCrationForm(request.POST or None)
    if request.method == 'POST':
        if itemsForm.is_valid():
            form.save()
            return redirect('view_products')
    context = {'form': form}
    return render(request, 'Rent_Anthing/register.html', context)


def login_user(request):
    form = AuthForm(request.POST or None)
    if request.method == 'POST':
        if itemsForm.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_products')
    context = {'form': form}
    return render(request, 'Rent_Anthing/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('items')