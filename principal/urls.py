from django.urls import path

from . import views

app_name = 'principal'
urlpatterns = [
    path("", views.index, name="index"),
    path("salesHistory/", views.salesHistory, name="salesHistory"),
    path("enterSales/", views.enterSales, name="enterSales"),
    path("enterStock/", views.enterStock, name="enterStock"),
    path("stadistics/", views.stadistics, name="stadistics"),
]