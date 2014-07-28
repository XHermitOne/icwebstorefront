# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response

from . import models

import logging

logger = logging.getLogger('ic_debug_logger')

def main_view(request):
    """
    Главная страница.
    """
    context = {}
    context['catalog'] = models.icCatalog.objects.all()
    context['wares'] = models.icWare.objects.all()

    return render_to_response('index.html', context)
