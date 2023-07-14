from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('daraja/stk_push', views.stk_push_callback, name='stk_push_callback'),
]
