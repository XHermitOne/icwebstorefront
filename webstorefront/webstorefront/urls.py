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
    url(r'^ajaxneworder/(?P<ware_uuid>[^/]+)/$', webstorefront.views.ajax_new_order),
    url(r'^ajaxaddorder/(?P<ware_uuid>[^/]+)/(?P<order_uuid>[^/]+)/$', webstorefront.views.ajax_add_order),
    url(r'^ajaxperformorder/(?P<order_uuid>[^/]+)/$', webstorefront.views.ajax_perform_order),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^news/', webstorefront.views.news_view),
    url(r'^order/(?P<order_uuid>[^/]+)/$', webstorefront.views.order_view),
    #url(r'^about/', webstorefront.views.about_view),

    url(r'^$', webstorefront.views.main_view),

)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
