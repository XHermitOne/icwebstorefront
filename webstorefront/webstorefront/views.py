# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect

try:
    import json
except ImportError:
    from django.utils import simplejson as json

from . import models

import logging

import os.path

logger = logging.getLogger('ic_debug_logger')

def main_view(request):
    """
    Главная страница.
    """
    context = dict()
    context['catalog'] = models.icCatalog.objects.all()
    context['wares'] = models.icWare.objects.all()

    return render_to_response('index.html', context)

def ajax_get_content_data(request, catalog_uuid):
    """
    Получение содержания каталога через Ajax.
    @param  catalog_uuid: UUID выбранного каталога.
    """
    if request.method == 'GET':
        data = list()
        try:
            catalog = models.icCatalog.objects.get(uuid=catalog_uuid)
            for rec in catalog.wares.all().values():
                rec['img'] = os.path.basename(rec['img'])
                data.append(rec)
            logger.debug('Records <%s>' % data)
        except:
            logger.error('Get content data catalog <%s>' % catalog_uuid)
            raise
        return HttpResponse(json.dumps(data), content_type='application/json')

    logger.error('Get content data catalog <%s> POST query' % catalog_uuid)
    return HttpResponse('error')
