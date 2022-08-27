from random import randint, shuffle, choice
from django.views.generic.base import TemplateView
from django.shortcuts import render

def glowwiththeflow(request):
    return render(request, 'justajolt_home/glowwiththeflow.html')

def joltfolio(request):
    return render(request, 'justajolt_home/joltfolioMultiBoot.html')

class JoltfolioSpecificView(TemplateView):
    modules = ()
    template_name = 'justajolt_home/joltfolioMultiBoot.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # get context
        context['machine'] = self.modules
        return context # if not, we're just passing in nothing!

def tang(request):
    return render(request, 'justajolt_home/home.html')

def target_range(request):
    return render(request, 'justajolt_home/target_range.html')

def portfolio(request):
    return render(request, 'justajolt_home/portfolio.html')

