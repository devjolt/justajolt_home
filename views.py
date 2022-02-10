from django.shortcuts import render

def home(request):
    return render(request, 'justajolt_home/home.html')


def target_range(request):
    return render(request, 'justajolt_home/target_range.html')

def joltfolio(request):
    return render(request, 'justajolt_home/joltfolio.html')
    
def portfolio(request):
    return render(request, 'justajolt_home/portfolio.html')

