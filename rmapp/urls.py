from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'rmapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('buy/',views.buy,name='buy'),
    path('sell/<int:id>/',views.sell,name='sell'),
    path('update/<int:id>/',views.update,name='update'),
]