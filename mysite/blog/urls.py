from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='blog'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('<int:article_id>/', view_articles, name='view_articles'),

]
