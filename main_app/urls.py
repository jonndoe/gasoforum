from django.conf.urls import url
from . import views

urlpatterns = [
    #home page
    url(r'^$', views.index, name='index'),
    url(r'^gasthemes/$', views.gasthemes, name='gasthemes'),
    url(r'^gastopics/$', views.gastopics, name='gastopics'),
    url(r'^photoalbums/$', views.photoalbums, name='photoalbums'),
    url(r'^photoalbums/(?P<photoalbum_id>\d+)/$', views.photoalbum, name='photoalbum'),
    url(r'^gasthemes/(?P<gastheme_id>\d+)/$', views.gasthemetext, name='gasthemetext'),
    url(r'^gastopics/(?P<gastopic_id>\d+)/$', views.gastopictext, name='gastopictext'),
    url(r'^new_gastheme/$', views.new_gastheme, name='new_gastheme'),
    url(r'^new_gastopic/$', views.new_gastopic, name='new_gastopic'),
    url(r'^new_photoalbum/$', views.new_photoalbum, name='new_photoalbum'),
    url(r'^new_photo/(?P<photoalbum_id>\d+)/$', views.new_photo, name='new_photo'),
    url(r'^new_gasthemetext/(?P<gastheme_id>\d+)/$', views.new_gasthemetext, name='new_gasthemetext'),
    url(r'^new_gastopictext/(?P<gastopic_id>\d+)/$', views.new_gastopictext, name='new_gastopictext'),
    url(r'^edit_gasthemetext/(?P<gasthemetext_id>\d+)/$', views.edit_gasthemetext, name='edit_gasthemetext'),
    url(r'^edit_gastopictext/(?P<gastopictext_id>\d+)/$', views.edit_gastopictext, name='edit_gastopictext'),
    url(r'^new_gasthemecomment/(?P<gastheme_id>\d+)/$', views.new_gasthemecomment, name='new_gasthemecomment'),
    url(r'^new_gasthemecommentreply/(?P<gasthemecomment_id>\d+)/$', views.new_gasthemecommentreply, name='new_gasthemecommentreply'),
    url(r'^new_gastopiccomment/(?P<gastopic_id>\d+)/$', views.new_gastopiccomment, name='new_gastopiccomment'),
]
