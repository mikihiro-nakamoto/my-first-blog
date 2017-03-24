from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import list

def name_list(request):
    lists = list.objects.filter(published_date__lte=timezone.now()).order_('published_date')
    return render(request, 'list/name_list.html', {'lists': lists})

def name_list(request):
    return render(request, 'list/name_list.html',{})

def list_detail(request, pk):
    list = get_object_or_404(list, pk=pk)
    return render(request, 'list/list_detail.html', {'list': list})
# Create your views here.
