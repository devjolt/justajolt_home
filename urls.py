from django.urls import path
from . import views

#justajolt/
urlpatterns = [
    path('', views.home, name='home'),
    path('joltfolio/', views.joltfolio, name='joltfolio'),
    path('portfolio/', views.portfolio, name='portfolio'),
]