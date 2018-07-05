from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^basic.html/', views.algo_op, name='algo_op')
]
