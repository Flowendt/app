from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Home page')

def about(request):
    context = {
        'title':'Базовая разметка HTML',
        'content':'Бесплатные уроки по программированию и HTML для новичков'
    }
    return render (request,'main/index.html',context)