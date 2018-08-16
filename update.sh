rm -r build/ dist django_jsoneditor_widget.egg-info && python setup.py sdist bdist_wheel && twine upload dist/*
