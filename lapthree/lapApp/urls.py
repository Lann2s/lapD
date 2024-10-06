from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),  
    path('<int:amount>', views.calculate_tax ),  
    path('taxrate', views.show_tax_rate), 
]