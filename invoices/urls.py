from django.urls import path
from . import views

urlpatterns = [
   path("", views.CreateInvoiceView.as_view(), name="home"),
]
