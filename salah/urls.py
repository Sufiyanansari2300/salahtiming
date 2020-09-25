from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('display/',views.display, name='display'),
    path('search/',views.search, name='search'),
    path('searchdisplay/',views.searchdisplay, name='searchdisplay'),
]
