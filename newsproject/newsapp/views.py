from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.

def index(request):
    newsapi = NewsApiClient(api_key='33a71091ab3548f1a05422a28e6866d9')
    top = newsapi.get_top_headlines(sources="business-insider,crypto-coins-news")
    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)

    return render(request,'newsapp/index.html',context={'mylist':mylist})