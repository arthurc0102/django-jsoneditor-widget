from django.contrib.admin import ModelAdmin
from django.contrib.postgres.fields import JSONField

from .forms import JSONEditor

__all__ = [
    'JSONFieldAdminMixin',
    'JSONFieldModelAdmin',
]


class JSONFieldAdminMixin:
    formfield_overrides = {
        JSONField: {
            'widget': JSONEditor,
        },
    }


class JSONFieldModelAdmin(JSONFieldAdminMixin, ModelAdmin):
    pass
