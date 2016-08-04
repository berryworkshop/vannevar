from django.conf.urls import url
from .views import ArticleView, ArticlesView

urlpatterns = [
    url(r'^articles/$', ArticlesView.as_view()),
]