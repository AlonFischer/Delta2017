from django.conf.urls import url
from delta import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]