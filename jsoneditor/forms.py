from django.forms import Textarea


class JSONEditor(Textarea):
    template_name = 'jsoneditor/jsoneditor.html'

    class Media:
        css = {
            'all': (
                'jsoneditor/jsoneditor.min.css',
            ),
        }

        js = (
            'jsoneditor/jsoneditor.min.js',
        )
