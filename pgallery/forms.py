# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.utils.translation import ugettext_lazy as _

from .models import Photo


class PhotoForm(forms.ModelForm):
    tags = SimpleArrayField(forms.CharField(), label=_("tags"), required=False)

    class Meta:
        model = Photo
        fields = ['title', 'image', 'tags']
