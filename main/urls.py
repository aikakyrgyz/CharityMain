
from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', MainPageView.as_view(), name = 'home'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name = 'category'),
    path('article/<int:pk>/', article_detail, name = 'article'),
    path('create-post/', create_post, name ='create_post'),
    path('update-post/<int:pk>/', update_post, name = 'update_post'),
    path('favorite-post/<int:pk>/', favorite_post, name='favorite_post'),
    path('delete-post/<int:pk>/', DeleteArticleView.as_view(), name='delete_post'),
    path('blogpost-like/<int:pk>/', PostLike, name='blogpost_like'),
    path('favorites/', post_favorite_list, name='post_favorite_list'),
    path('donate/', make_donation, name = 'make_donation'),
    path('donate-petition/<int:pk>/', make_donation_petition, name = 'make_donation_petition'),
    path('petition/', create_petition, name='create_petition'),
    path('petition/<int:pk>', petition_detail, name='petition_detail'),
    # path('petition-like/<int:pk>', PetitionLike, name='petition_like'),

]