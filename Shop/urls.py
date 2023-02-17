from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='Prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>', views.prodDetails, name='details'),
    path('search', views.searching, name='search'),

]
