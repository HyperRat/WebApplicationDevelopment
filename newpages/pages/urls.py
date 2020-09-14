from django.urls import path

from .views import HomePageView, AboutPageView, HehePageView

urlpatterns = [
    path('hehe/', HehePageView.as_view(), name='hehe'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'), 
]
