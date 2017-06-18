from django.conf.urls import url, include

from . import views
app_name = 'polls'
urlpatterns = [
     url(r'^polls/', include('polls.urls', namespace="polls")),
    #ex: /polls
    url(r'^$', views.IndexView.as_view(), name='index'),
    #ex : /polls/5
    url(r'^(?P<pk>[0-9]+)/$' , views.DetailView.as_view() , name = 'detail'),
    url(r'^(?P<pk>[0-9]+)/results/$' , views.ResultViews.as_view() , name = 'results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$' , views.vote , name = 'vote'),
]