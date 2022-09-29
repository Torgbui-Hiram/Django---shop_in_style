from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('add-product', views.add_product, name='product'),
    path('show-product/<product_id>', views.show_product, name='show-product'),
    path('update-product/<product_id>', views.update_product, name='update'),
    path('search_all', views.new_product, name='new'),
]
