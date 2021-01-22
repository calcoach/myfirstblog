from django.conf.urls import url, include
from apps.app1.views import index
from apps.app1.views import privacypolicy

urlpatterns= [
    url(r'^', index),
    url(r'^', privacypolicy, name = 'privacypolicy'),

]
