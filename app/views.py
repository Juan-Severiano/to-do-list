from django.shortcuts import render
from .models import ItemList
from datetime import datetime

data_atual = datetime.today()

def home(request):
    item_list = ItemList.objects.filter(due_date__gt=data_atual).order_by('due_date')
    item_list_today = ItemList.objects.filter(due_date=data_atual).order_by('-due_date')
    item_list_past = ItemList.objects.filter(due_date__lt=data_atual).order_by('-due_date')
    return render(request, 'pages/home.html', context={
        'item_list': item_list,
        'atual_date': data_atual,
        'item_list_past':item_list_past,
        'item_today': item_list_today,
    })


def to_do(request):
    item_list = ItemList.objects.filter(due_date__gt=data_atual).order_by('due_date')
    return render(request, 'pages/to_do.html', context={
        'item_to_do': item_list,
    })