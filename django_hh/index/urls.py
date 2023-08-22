from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('about', views.about),
    path('contacts', views.contacts),
    path('news_home', views.news_home),
    path('category/<int:pk>', views.get_exact_category),
    path('product/<int:pk>', views.get_exact_product, name='news-detail'),
    path('search', views.search_product),
]
