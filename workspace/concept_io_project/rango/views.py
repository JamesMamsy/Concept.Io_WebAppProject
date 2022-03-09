from django.shortcuts import render
from django.models import Page

def index(request):

    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['pages'] = [page_list]
    return render(request, 'rango/index.html', context = context_dict)

