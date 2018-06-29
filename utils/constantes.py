# -*- coding: UTF-8 -*-
from django.utils.html import format_html

__ICONS__ = {
    'ATPasta': '<i class=\"fa fa-folder-o\" aria-hidden=\"true\"></i>',
    'ATPagina': '<i class=\"fa fa-file-text-o\" aria-hidden=\"true\"></i>',
    'ATNoticia': '<i class=\"fa fa-newspaper-o\" aria-hidden=\"true\"></i>',
    'ATImagem': '<i class=\"fa fa-file-image-o\" aria-hidden=\"true\"></i>',
    'ATLink': '<i class=\"fa fa-link\" aria-hidden=\"true\"></i>',
    'ATBanner': '<i class=\"fa fa-image\" aria-hidden=\"true\"></i>',
    'ATArquivo': '<i class=\"fa fa-file-o\" aria-hidden=\"true\"></i>',
    'ATEvento': '<i class=\"fa fa-calendar-o\" aria-hidden=\"true\"></i>',
    'ATAgenda': '<i class=\"fa fa-calendar\" aria-hidden=\"true\"></i>',
    'ATInforme': '<i class=\"fa fa-tv\" aria-hidden=\"true\"></i>',
    'ATServico': '<i class=\"fa fa-fax\" aria-hidden=\"true\"></i>',
}


def get_icon(tipo):
    return format_html(__ICONS__[tipo])
