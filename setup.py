"""
flask-csrf
----------

A small Flask extension for adding CSRF protection. Runscope fork.

Original Links
``````````````

* `documentation <http://sjl.bitbucket.org/flask-csrf/>`_
* `development version
  <http://bitbucket.org/sjl/flask-csrf/get/tip.gz#egg=flask-csrf-dev`_


"""
from setuptools import setup


setup(
    name='flask-csrf',
    version='0.9.2.1',
    url='https://github.com/Runscope/flask-csrf',
    license='MIT',
    author='Ryan Park',
    author_email='ryan@runscope.com',
    description='A small Flask extension for adding CSRF protection.',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>0.1'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
