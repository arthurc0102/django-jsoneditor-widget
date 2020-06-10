# django-jsoneditor-widget

> Django form widget form JSONField

## Demo

It look like this.

![demo image](https://github.com/arthurc0102/django-jsoneditor-widget/blob/master/screenshot/demo.png?raw=true)

## Install

- Install: `pip install django-jsoneditor-widget`
- Settings:
    ```python
    INSTALLED_APPS = [
        # some apps ....
        'jsoneditor',
        # other apps ...
    ]
    ```

## Create model

```python
from django.db import models
from django.contrib.postgres.fields import JSONField


class Book(models.Model):
    name = models.CharField(max_length=150)
    information = JSONField()

    def __str__(self):
        return self.name
```

## Admin site settings

- Use ModelAdmin
    ```python
    from django.contrib import admin

    from jsoneditor.admin import JSONFieldModelAdmin

    from .models import Book


    admin.site.register(Product, JSONFieldModelAdmin)
    ```

- Use mixin
    ```python
    from django.contrib import admin
    
    from jsoneditor.admin import JSONFieldAdminMixin

    from .models import Book


    @admin.register(Book)
    class BookModelAdmin(JSONFieldAdminMixin, admin.ModelAdmin):
        pass
    ```

- Use custom widget to specify jsoneditor options
    ```python
    from django.contrib import admin
    from django.contrib.postgres.fields import JSONField

    from jsoneditor.forms import JSONEditor

    from .models import Book


    class TextJSONEditor(JSONEditor):
        jsoneditor_options = {
            "mode": "text"
        }


    @admin.register(Book)
    class BookModelAdmin(admin.ModelAdmin):
        formfield_overrides = {
            JSONField: {"widget": TextJSONEditor}
        }

    ```
