import jsoneditor

from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='django-jsoneditor-widget',
    license='MIT',
    version=jsoneditor.__version__,

    author='Arthur Chang',
    author_email='arthurc0102@gmail.com',
    url='https://github.com/arthurc0102/django-jsoneditor-widget',

    packages=['jsoneditor'],
    description='Django form widget form JSONField',
    long_description=long_description,
    include_package_data=True,
)