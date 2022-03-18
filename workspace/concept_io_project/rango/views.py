from django.shortcuts import render

# Create your views here.
def view_categories(request):
    context_dict = {}

    categories=Category.objects.all()
    conttext_dict['categories']=categories

    return render(request, 'rango/categories.html',context_dict)



