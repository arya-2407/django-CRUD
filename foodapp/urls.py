from . import views
from django.urls import path

app_name = 'foodapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('item/',views.item,name='item'),
    path('item/<int:item_id>/',views.detail,name='detail'),
    path('item/add/', views.create_item, name='create_item'),
    path('item/update/<int:item_id>/',views.update_item,name='update_item'),
    path('item/delete/<int:item_id>', views.delete_item,name='delete_item')
]
