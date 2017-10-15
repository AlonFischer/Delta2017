from django.conf.urls import url
from delta import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()),
    url(r'^seats$', views.surveyProcess),
    url(r'^submit', views.seatFinish),
    # url(r'^seats$', views.seatSelection)
]