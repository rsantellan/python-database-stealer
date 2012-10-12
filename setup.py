#! /usr/bin/python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description' : "My project",
    'author' : "Rodrigo Santellan",
    'url' : "myurl.com",
    'download_url' : 'myurl.com',
    'author_email' : 'rsantellan@gmail.com',
    'version' : '0.0.1',
    'install_requieres' : ['nose'],
    'packages' : ['NAME'],
    'scripts' : [],
    'name' : 'Mi proyecto'
}

setup(**config)
