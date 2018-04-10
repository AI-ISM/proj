import json
from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib.request


def index(request):
    # Reading data back
    with open('app/static/json/blogList.json', 'rb') as f:
        resp = json.load(f)

    return HttpResponse(json.dumps(resp), content_type="application/json")


def item(request, article_id):
    url = 'http://wcf.open.cnblogs.com/blog/post/body/' + str(article_id)
    req = urllib.request.Request(url)
    webpage = urllib.request.urlopen(req)
    html = webpage.read()
    soup = BeautifulSoup(html, 'html.parser')  # 文档对象
    data = soup.find_all('string')[0].string

    return HttpResponse(data)
