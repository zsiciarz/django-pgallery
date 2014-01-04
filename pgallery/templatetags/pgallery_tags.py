# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2014.

from __future__ import unicode_literals

from django import template
from django.db import connection

from pgallery.models import Gallery, Photo

register = template.Library()


@register.assignment_tag
def get_recent_galleries(count=3):
    """
    Returns most recent galleries.
    """
    return Gallery.objects.published().order_by('-shot_date')[:count]


@register.assignment_tag
def get_gallery_archive_dates():
    """
    Returns datetime objects for all months in which galleries were added.
    """
    return Gallery.objects.published().dates('shot_date', 'month', order='DESC')


@register.assignment_tag
def get_popular_tags(count=10):
    """
    Returns most popular tags.
    """
    query = """
    select
        t.tag,
        count(t.tag) as tag_count
    from
        (select unnest(tags) as tag from %s) t
    group by tag
    order by tag_count desc
    limit %%s
    """ % Photo._meta.db_table
    cursor = connection.cursor()
    cursor.execute(query, (count,))
    tags = [{'tag': row[0], 'count': row[1]} for row in cursor.fetchall()]
    return tags
