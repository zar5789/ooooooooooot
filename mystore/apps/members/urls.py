from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/',views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('add/myfirst/', views.back_main, name='home'),
    path('search/', views.search_record, name='search_record'),
    path('search/myfirst/', views.back_main, name='home2'),
    path('update/<int:id>', views.edit, name='update'),
    path('update/myfirst/', views.back_main, name='home3'),
    path('update/edit_record/<int:id>', views.edit_record, name='edit_record'),
    path('delete/<int:id>', views.remove_record, name='remove_record')
    

    ]