from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('cart/<int:item_id>/', views.cart, name='cart'),
    path('items/<str:term1>/', views.term1, name='term1'),
    path('terms2/<str:term2>/', views.term2, name = "term2"),
    path('terms3/<str:term3>/', views.term3, name = "term3"),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)