import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="DuerOS-Python-Servcer",
    version="0.0.1",
    author="Fred Liang",
    author_email="info@fredliang.cn",
    description=("DuerOS server deploy example"),
    license="BSD",
    packages=["Flask",
              "Flask_SQLAlchemy",
              "gunicorn",
              "rsa",
              "Flask_PyMongo",
              "requests",
              "mysql-connector-python-rf"],
    long_description=read('README.md'),
)
