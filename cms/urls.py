from django.conf.urls import url
from .views import HomeView, ArticleView, ArticlesView

urlpatterns = [
    url(r'^articles/$', ArticlesView.as_view()),
    url(r'', HomeView.as_view()),
]