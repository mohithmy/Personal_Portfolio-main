from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.all_blogs, name = 'all_blogs'),
    path('<int:blog_id>',views.details, name='details'),
]