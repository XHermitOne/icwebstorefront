from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

import webstorefront.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webstorefront.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #Ajax-запросы
    url(r'^ajaxgetcontent/(?P<catalog_uuid>[^/]+)/$', webstorefront.views.ajax_get_content_data),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^news/', webstorefront.views.news_view),

    url(r'^$', webstorefront.views.main_view),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
