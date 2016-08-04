from django.views.generic import TemplateView


class ArticleView(TemplateView):
    template_name = "cms/article.html"


class ArticlesView(TemplateView):
    template_name = "cms/articles.html"