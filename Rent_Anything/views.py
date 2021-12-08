from django.shortcuts import render, redirect
from .forms import itemsForm, UserCrationForm, AuthForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import items


def view_products(request):
    item = items.objects.all()
    form = itemsForm()
    context = {'items': item, 'form': form}
    return render(request, 'Rent_Anthing/items.html', context)


@login_required(login_url='login')
def view_more(request, id):
    item = items.objects.get(id=id)
    form = itemsForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('view_products')
    return render(request, 'Rent_Anthing/more.html', {'item': item})


@login_required(login_url='login')
def create_product(request):
    if request.method == 'POST':
        form = itemsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('view_products')
    else:
        form = itemsForm()
    return render(request, 'Rent_Anthing/product-form.html', {'form': form})


def update_product(request, id):
    product = items.objects.get(id=id)
    form = itemsForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('view_products')

    return render(request, 'Rent_Anthing/product-form.html', {'form': form})


@login_required(login_url='login')
def delete_product(request, id):
    product = items.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('view_products')

    return render(request, 'Rent_Anthing/delete-confirm.html', {'product': product})


def register_user(request):
    form = UserCrationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_products')
    context = {'form': form}
    return render(request, 'Rent_Anthing/register.html', context)


def login_user(request):
    form = AuthForm(data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_products')
    context = {'form': form}
    return render(request, 'Rent_Anthing/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('view_products')
