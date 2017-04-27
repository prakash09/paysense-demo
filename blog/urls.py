from django.conf.urls import  include, url
from .views import *
from django.conf import settings


urlpatterns = [
	url(r'^$',listAllPosts,name='list_all_posts'),
	url(r'^save/$',savePost,name='save_posts'),
	url(r'^delete/$',deletePosts,name='delete_post'),
	url(r'^delete/(?P<post_id>[0-9]+)/$',deletePosts,name='delete_post'),
]

