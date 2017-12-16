from django.conf.urls import include, url
from chart import views

urlpatterns = [
    url(r'^chart$',views),
]