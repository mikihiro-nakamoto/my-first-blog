from django.shortcuts import render
from django.utils import timezone
from .models import list

def name_list(request):
    lists = list.objectsself.filter(published_date__lte=timezone.now()).order_('published_date')
    return render(request, 'list/name_list/html', {'lists': lists})

# Create your views here.
