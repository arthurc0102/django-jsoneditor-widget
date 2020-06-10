import json

from django.forms import Textarea


class JSONEditor(Textarea):
    template_name = 'jsoneditor/jsoneditor.html'
    jsoneditor_options = {}

    def get_context(self, name, value, attrs):
        ctx = super().get_context(name, value, attrs)
        ctx.update(
            {
                'jsoneditor_options': json.dumps(self.jsoneditor_options),
            },
        )
        return ctx

    class Media:
        css = {
            'all': ('jsoneditor/jsoneditor.min.css', ),
        }

        js = ('jsoneditor/jsoneditor.min.js', )
