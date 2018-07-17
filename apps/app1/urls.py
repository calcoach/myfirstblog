from django.conf.urls import url, include
from apps.app1.views import index

urlpatterns= [
    url(r'', index)

]