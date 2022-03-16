from django.shortcuts import render
from django.models import Page

def index(request):

    page_list = Page.objects.order_by('-views')[0:10]
    design_day = Page.objects.order_by('-likes')[:1]
    #new additions = Page.objects.order_by('-datetime')[0:10]
    context_dict = {}
    context_dict['dotd'] = [design_day]
    context_dict['pages'] = [page_list]
    #context_dict['additions'] = [new pages]
    return render(request, 'rango/index.html', context = context_dict)
