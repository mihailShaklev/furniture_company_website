""" furniture URL configuration """
from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('kitchen', views.Kitchens, name='kitchens'),
    path('furniture', views.Furniture, name='furniture'),
    path('contact-form', views.FormHandler, name='contact_form')
]