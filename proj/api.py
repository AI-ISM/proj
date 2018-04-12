from django.conf.urls import url
from django.urls import path
from app.api import article
from app.api import leetcode

app_name = 'proj'
urlpatterns = [
    path('article/index', article.index),
    path('article/item/<int:article_id>', article.item),
    path('leetcode/question_all', leetcode.question_all),
    path('leetcode/question/<str:title_slug>', leetcode.question),
]
