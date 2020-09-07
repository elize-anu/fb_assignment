# from django.urls import include, path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from fbMyApp import views

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    url(r'^social-auth/', include('social_django.urls', namespace='social')),
    url(r'^fetch_posts/', views.fetch_posts_from_page,name='fetch_posts_from_page'),

]