# -*- coding: UTF-8 -*-
from django.utils.html import format_html
import warnings

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


def deprecated(func):
    """This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emmitted
    when the function is used."""
    def newFunc(*args, **kwargs):
        warnings.warn("Call to deprecated function %s." % func.__name__,
                      category=DeprecationWarning)
        return func(*args, **kwargs)
    newFunc.__name__ = func.__name__
    newFunc.__doc__ = func.__doc__
    newFunc.__dict__.update(func.__dict__)
    return newFunc