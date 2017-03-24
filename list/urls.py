from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.name_list, name='name_list'),
     url(r'^list/(?P<pk>\d+)/$', views.list_detail, name='list_detail'),
]
