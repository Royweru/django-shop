from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contact/', views.contact, name='contact'),
    path('why/', views.why, name='why'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('shop/', views.shop, name='shop'),
]
