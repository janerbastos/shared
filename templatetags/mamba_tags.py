# -*- coding:UTF-8 -*-

from django import template
from django.utils.html import format_html

from mamba.models import Site

register = template.Library()


@register.assignment_tag()
def has_total_sites():
    return Site.objects.all().count()
