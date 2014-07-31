# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core import paginator

try:
    import json
except ImportError:
    from django.utils import simplejson as json

from . import models

import logging

import os.path

logger = logging.getLogger('ic_debug_logger')


def prepare_wares(request, catalog_uuid=None):
    """
    Подготовка товаров для добавления их в контекст.
    """
    data = list()
    try:
        if catalog_uuid is None:
            wares = models.Ware.objects.all()
        else:
            catalog = models.Catalog.objects.get(uuid=catalog_uuid)
            wares = catalog.wares.all()

        search_txt = request.GET.get('search')
        if search_txt:
            wares = wares.filter(label__icontains=search_txt)

        for rec in wares.values():
            rec['img'] = os.path.basename(rec['img'])
            data.append(rec)
        logger.debug('Records <%s>' % data)
        return data
    except:
        logger.error('Get content data catalog <%s>' % catalog_uuid)
        raise
    return []


def main_view(request):
    """
    Главная страница.
    """
    context = dict()
    context['catalog'] = models.Catalog.objects.all()
    context['wares'] = prepare_wares(request)

    return render_to_response('index.html', context)


def ajax_get_content_data(request, catalog_uuid):
    """
    Получение содержания каталога через Ajax.
    @param  catalog_uuid: UUID выбранного каталога.
    """
    if request.method == 'GET':
        data = prepare_wares(request, catalog_uuid)
        return HttpResponse(json.dumps(data), content_type='application/json')

    logger.error('Get content data catalog <%s> POST query' % catalog_uuid)
    return HttpResponse('error')


def news_view(request):
    """
    Страница новостей.
    """
    rec_news = models.New.objects.all()
    tag_filter = request.GET.get('tag_filter')

    if tag_filter:
        rec_news = rec_news.filter(tags__in=tag_filter)

    search_txt = request.GET.get('search')
    if search_txt:
        rec_news = rec_news.filter(title__icontains=search_txt)

    news_paginator = paginator.Paginator(rec_news, 10)

    page = request.GET.get('page')
    try:
        news = news_paginator.page(page)
    except paginator.PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = news_paginator.page(1)
    except paginator.EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = news_paginator.page(news_paginator.num_pages)

    context = dict()
    context['news'] = news
    context['tags'] = models.NewsTag.objects.all()

    return render_to_response('news.html', context)
