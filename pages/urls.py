from django.conf.urls import url

from . import views

app_name = 'pages'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^career/$', views.career, name='career'),
    url(r'^investments/$', views.actives, name='actives'),
    url(r'^contacts/$', views.contacts, name='contacts'),
    # почти
    url(r'^investments/(?P<id>[-\w]+)$', views.active, name='active'),
    url(r'^team/$', views.team, name='team'),
    url(r'^team/(?P<name>[-\w]+)$', views.person, name='persn'),
    url(r'^consulting/', views.consulting, name='consulting'),
    url(r'^news/$', views.news, name='news'),
    url(r'^news/(?P<id>[-\w]+)$', views.new, name='new'),

    # ничего не сделал
    url(r'^docs/$', views.docs, name='docs'),
    url(r'^expertise/$', views.expertise, name='expertise'),
    url(r'^expertise/(?P<id>[-\w]+)$', views.expertise_page, name='expertise_page'),
    url(r'^search/$', views.search, name='search'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^projects/(?P<id>[-\w]+)$', views.active, name='project'),
    
    
    
    
    url(r'^send_resume/$', views.send_resume, name='send_resume'),
    url(r'^filter_projects/$', views.filter_projects, name='filter_projects'),
    url(r'^filter_news/$', views.filter_news, name='filter_news'),
 

]
