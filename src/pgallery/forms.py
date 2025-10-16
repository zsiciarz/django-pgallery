from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from django.utils.translation import gettext_lazy as _

from .models import Photo


class PhotoForm(forms.ModelForm):
    tags = SimpleArrayField(forms.CharField(), label=_("tags"), required=False)

    class Meta:
        model = Photo
        fields = ["title", "image", "tags"]
