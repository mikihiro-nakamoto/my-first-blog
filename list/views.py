from django.shortcuts import render
from django.utils import timezone
from .models import list

def name_list(request):
    lists = list.objects.filter(published_date__lte=timezone.now()).order_('published_date')
    return render(request, 'list/name_list.html', {'lists': lists})

def name_list(request):
    return render(request, 'list/name_list.html',{})
# Create your views here.
