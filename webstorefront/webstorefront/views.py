# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, Http404
from django.core import paginator
from django.db.models import Sum
from django.conf import settings

try:
    import json
except ImportError:
    from django.utils import simplejson as json

from . import models
from . import utils

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
    context['pos_count'] = models.Order.objects.get(uuid=request.session['CURRENT_ORDER']).positions.all().count() if 'CURRENT_ORDER' in request.session else 0

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
    return Http404()


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
    context['pos_count'] = models.Order.objects.get(uuid=request.session['CURRENT_ORDER']).positions.all().count() if 'CURRENT_ORDER' in request.session else 0

    return render_to_response('news.html', context)


def ajax_new_order(request, ware_uuid):
    """
    Добавить новый заказ через Ajax.
    @param  ware_uuid: UUID выбранного товара.
    """
    logger.debug('START new order')
    if request.method == 'GET':
        try:
            #Определить нужный нам заказ
            order = models.Order()
            order.save()
            #Добавить позицию заказа если новый товар
            ware = models.Ware.objects.get(uuid=ware_uuid)
            pos = order.positions.create(ware_uuid=ware_uuid, count=1, summ=ware.price)
            pos.save()

            request.session['CURRENT_ORDER'] = order.uuid

            data = {'order_uuid': order.uuid, 'pos_count': order.positions.all().count()}
            return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            logger.error('New order')
            #return Http404()
            raise

    logger.error('New order GET query')
    return Http404()


def ajax_add_order(request, ware_uuid, order_uuid):
    """
    Добавить товар в заказ через Ajax.
    @param  ware_uuid: UUID выбранного товара.
    """
    logger.debug('START')
    if request.method == 'GET':
        try:
            #Определить нужный нам заказ
            order = models.Order.objects.get(uuid=order_uuid)

            ware = models.Ware.objects.get(uuid=ware_uuid)
            positions = order.positions.all().filter(ware_uuid=ware_uuid)
            if positions:
                #Если позиция с таким товаром есть то просто увеличить
                #количество и сумму позиции
                pos = positions[0]
                pos.count += 1
                pos.summ += ware.price
            else:
                pos = order.positions.create(ware_uuid=ware_uuid, count=1, summ=ware.price)
            pos.save()

            data = {'order_uuid': order.uuid, 'pos_count': order.positions.all().count()}
            #logger.debug('Count data %s' % data)
            return HttpResponse(json.dumps(data), content_type='application/json')
        except:
            logger.error('Add ware in order <%s>' % order_uuid)
            #return Http404()
            raise

    logger.error('Add ware in order <%s> GET query' % order_uuid)
    return Http404()


def order_view(request, order_uuid):
    """
    Страница заказа.
    """
    logger.info('Request: %s' % request)
    order = models.Order.objects.get(uuid=order_uuid)

    context = dict()
    context['order'] = order

    positions=[]
    for rec in order.positions.all().values():
        rec['ware_label'] = models.Ware.objects.get(uuid=rec['ware_uuid'])
        positions.append(rec)
    context['positions'] = positions
    context['pos_count'] = order.positions.all().count()
    context['sum_result'] = order.positions.all().aggregate(sum_result=Sum('summ'))['sum_result']

    return render_to_response('order.html', context)


def ajax_perform_order(request, order_uuid):
    """
    Отправить сообщение на подтверждение заказа исполнителю через Ajax.
    """
    order = models.Order.objects.get(uuid=order_uuid)
    text = u'\n'.join(['%s\t%s\t%s' % (models.Ware.objects.get(uuid=pos.ware_uuid).label, pos.count, pos.summ) for pos in order.positions.all()])
    utils.send_email(settings.EMAIL_FROM, settings.EMAIL_TO,
                     u'Заказ', text.encode(settings.DEFAULT_ENCODING))
    return HttpResponse('OK')
