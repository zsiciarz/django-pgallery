# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2015.

from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from djorm_pgarray.fields import ArrayFormField

from .models import Photo


class PhotoForm(forms.ModelForm):
    tags = ArrayFormField(label=_("tags"), required=False)

    class Meta:
        model = Photo
        fields = ['title', 'image', 'tags']
