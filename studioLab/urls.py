from django.conf.urls import url
from .views import pobal_studio

urlpatterns = [
    url(r'^pobal_studio/$', pobal_studio, name='pobal_studio'),
]