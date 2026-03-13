from django.shortcuts import render
from .models import Article


def article_list(request):

    articles = Article.objects.filter(is_published=True)

    template_name="app/index.html"

    context = {
        "articles_list": articles
    }

    return render(
        request=request,
        template_name=template_name,
        context=context,
        )
