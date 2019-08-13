from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from feed import views as feed_views
#from feed import views as fetch_toUI
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
     url(r'^$', feed_views.RendertoUI, name='RendertoUI'),
	 url(r'RendertoUI/$', feed_views.searchposts, name='searchposts'),
	#url(r'^Newsinfo/$', feed_views.Newsinfo, name='Newsinfo'),
	#url(r'^Call/$', feed_views.Call, name='call'),
	#url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	#url(r'^uploads/simple/$', core_views.simple_upload, 
	]