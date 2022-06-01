from django.shortcuts import render
from .models import Article, Category


def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles, 'title': 'Блог'})


def get_category(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'blog/category.html',
                  {'articles': articles, 'title': category.title, 'category': category})


def view_articles(request, article_id):
    articles_item = Article.objects.get(pk=article_id)
    return render(request, 'blog/view_articles.html', {"articles_item": articles_item})
