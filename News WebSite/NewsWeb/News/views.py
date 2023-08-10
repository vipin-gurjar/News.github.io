from django.shortcuts import render
from multiprocessing import context
import requests
import json
Api_Key = "8b29e7a1fffe405fba05b39cd7637de7"

# Create your views here.
def Index(request):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={Api_Key}"
    data=requests.get(url)
    Response=data.json()
    articles=Response['articles']
    context={
         'articles':articles
        }
    return render (request,'index.html',context)


def Category(request,name):
    url = f"https://newsapi.org/v2/top-headlines?category={name}&apiKey={Api_Key}"
    data=requests.get(url)
    Response=data.json()
    articles=Response['articles']
    context={
         'articles': articles,
         'category': name
        }
    return render (request,'category.html',context)


def Search(request):
    search_term=request.GET.get('search')
    url=f'https://newsapi.org/v2/everything?q={search_term}&apiKey={Api_Key}'
    data=requests.get(url)
    Response=data.json()
    articles=Response['articles']
    context={
        'articles':articles,
        'search':search_term
    }
    return render(request,'search.html',context)
        

def Country(request,name):
     url=f"https://newsapi.org/v2/top-headlines?country={name}&apiKey={Api_Key}"
     data=requests.get(url)
     Response=data.json()
     articles=Response['articles']
     context={
          'articles': articles,
          'country': name
        }
     return render (request,'country.html',context)


    

