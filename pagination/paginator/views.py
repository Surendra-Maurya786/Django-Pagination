from django.shortcuts import render
from .models import Path
from django.core.paginator import Paginator

# Create your views here.


def hello(request):

    all_post= Path.objects.all().order_by('id')
    paginator=Paginator(all_post,3)
    page_number= request.GET.get('page')
    page_obj= paginator.get_page(page_number)




    return render(request,"index.html",{'page_obj': page_obj})