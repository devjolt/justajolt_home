from django.urls import path
from . import views

#justajolt/
urlpatterns = [
    path('', views.joltfolio, name='joltnet'),
    path('tang/', views.home, name='home'),
    path('joltfolio2/', views.joltfolio2, name='joltfolio2'),
    path('generic/', views.joltfolioGeneric, name='joltfolioGeneric'),
    #path('target_range/', views.target_range, name='target_range'),
    #path('portfolio/', views.portfolio, name='portfolio'),
]