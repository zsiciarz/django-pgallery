from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

urlpatterns = [
    # Examples:
    # url(r'^$', 'example_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'', include('pgallery.urls', namespace='pgallery')),
]
