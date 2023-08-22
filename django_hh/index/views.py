from django.shortcuts import render, redirect
from . import forms, models
from . models import Product
import requests

from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
def home_page(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar, 'products': products, 'categories': categories}
    return render(request, 'index.html', context)

def news_home(request):
    search_bar = forms.SearchForm()
    products = models.Product.objects.all()
    categories = models.Category.objects.all()
    context = {'form': search_bar, 'products': products, 'categories': categories}
    return render(request, 'news_home.html', context)

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def get_exact_category(request, pk):
    category = models.Category.objects.get(id=pk)
    products = models.Product.objects.filter(product_category=category)
    context = {'products': products}
    return render(request, 'exact_category.html', context)

def get_exact_product(request, pk):
    product = models.Product.objects.get(id=pk)
    context = {'product': product}
    return render(request, 'exact_product.html', context)

def search_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')
        try:
            exact_product = models.Product.objects.get(product_name__icontains=get_product)
            return redirect(f'product/{exact_product.id}')
        except:
            return redirect('/')

def add_to_cart(request, pk):
    if request.method == 'POST':
        checker = models.Product.objects.get(id=pk)
        if checker.product_amount >= int(request.POST.get('product_amount')):
            models.Cart.objects.create(user_id=request.user.id, user_product=checker, user_product_count=int(request.POST.get('product_amount'))).save()
            return redirect('/')
        else:
            return redirect('/')

def user_cart(request):
    cart = models.Cart.objects.filter(user_id=request.user.id)
    context = {'cart': cart}
    return render(request, 'user_cart.html', context)

def del_from_cart(request, pk):
    product_to_delete = models.Product.objects.get(id=pk)
    models.Cart.objects.filter(user_id=request.user.id, user_product=product_to_delete).delete()
    return redirect('/cart')

def register(request):
    error = ''
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = forms.RegisterForm(request.POST)
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def get_weather(city):
    API_TOKEN = '7d58c54b3c0c66b13dcff13b9c5134e7'
    params = {'q': city, 'appid': API_TOKEN, 'units': 'metric'}
    response = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    x = response.json()
    if x['weather'][0]['main'] == 'Clear':
        p='ясно'
    else:
        p='облачно'
    print(f'Сегодня в городе {city} {p}')
    print('Температура:', x['main']['temp'], 'Градусов Цельсия')
    print('Атмосферное давление:', x['main']['pressure'], 'мм. рт. ст.')
    print('Влажность:', x['main']['humidity'], '%')
    print('Скорость ветра:', x['wind']['speed'], 'м/сек')

