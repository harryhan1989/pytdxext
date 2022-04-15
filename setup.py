#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='pytdxext',

    version='1.0.0',

    description='pytdxext',

    python_requires='>=3.6',

    author='lhan',
    author_email='850919407@qq.com',

    long_description='',
    long_description_content_type="text/markdown",

    license='',
    url="",
    project_urls={
    },

    # What does your project relate to?
    keywords=['trader'],

    packages=setuptools.find_packages(),

    install_requires=[
        'schedule',
        'psycopg2-binary',
        'akshare',
        'chinesecalendar',
        'baostock',
        'vthread',
        'backtrader[plotting]',
        'easytrader',
        'easyquotation'
    ],
)