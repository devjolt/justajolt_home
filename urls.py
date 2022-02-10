from django.urls import path
from . import views

#justajolt/
urlpatterns = [
    path('', views.joltfolio, name='joltnet'),
    path('tang/', views.home, name='home'),
    #path('target_range/', views.target_range, name='target_range'),
    #path('portfolio/', views.portfolio, name='portfolio'),
]