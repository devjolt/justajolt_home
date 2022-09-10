from django.urls import path
from . import views

machine_list = [
    'commodorePET2001',
    'commodore64',
    'windows1',
    'xedos81',
    'decvt320',
    'amstrad',
    'oric1',
    'generic',
    '90s',
    'tandyDos90',
    
]

#justajolt/
urlpatterns = [
    path('', views.joltfolio, name='joltnet'),
    path('tang/', views.tang, name='tang'),
    path('glowwiththeflow/', views.glowwiththeflow, name='glowwiththeflow'),
    #path('target_range/', views.target_range, name='target_range'),
    #path('portfolio/', views.portfolio, name='portfolio'),
]

for machine in machine_list:
    urlpatterns.append(path(f'{machine}/', views.JoltfolioSpecificView.as_view(modules = (machine)), name=f'booting {machine}'))