from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('val',views.val,name='value'),
    path('<str:id>',views.search,name='search'),
]
