from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "cms/home.html"


class ArticleView(TemplateView):
    template_name = "cms/article.html"


class ArticlesView(TemplateView):
    template_name = "cms/articles.html"