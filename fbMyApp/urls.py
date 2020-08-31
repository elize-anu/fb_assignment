# from django.urls import include, path
from django.conf.urls import url, include
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', TemplateView.as_view(template_name = 'home.html'), name = 'home'),
    url(r'^social-auth/', include('social_django.urls', namespace='social'))
]