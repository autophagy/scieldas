
# -*- coding: utf-8 -*-

from setuptools import setup

try:
    with open('README.rst', 'r', encoding='utf-8') as f:
        readme = f.read()
except IOError:
    readme = ''


setup(
    name='scieldas',
    author='Mika Naylor (Autophagy)',
    author_email='mail@autophagy.io',
    description='Flask-based README badge service, inspired by shields.io',
    long_description=readme,
    packages=['scieldas'],
    install_requires=[
        'Flask==0.12.2',
        'slumber==0.7.1',
        'svgwrite==1.1.11',
        'gunicorn==19.7.1',
    ],
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    use_scm_version=True
)
