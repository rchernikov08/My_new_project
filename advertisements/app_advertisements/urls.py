from django.urls import path
from .views import index, top_sellers, register, advertisement_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('register/', register, name = 'register'),
    path('advertisement-post/', advertisement_post, name = 'advertisement-post'),
]
