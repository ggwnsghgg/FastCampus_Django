from django.shortcuts import render
from .models import Board

# Create your views here.

def board_list(request):
    #order_by('-id') 는 가장 최신부터 불러오는 방법
    boards = Board.objects.all().order_by('-id')
    return render(request, 'board_list.html', {'boards': boards})   


