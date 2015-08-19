from setuptools import setup, find_packages

import ast


def readme():
    try:
        f = open('README.rst')
    except IOError:
        return
    try:
        return f.read()
    finally:
        f.close()


def get_version():
    with open(filename) as f:
        tree = ast.parse(f.read(), filename)
        for node in tree.body:
            if (isinstance(node, ast.Assign) and
                    node.targets[0].id == '__version__'):
                version = ast.literal_eval(node.value)
        if isinstance(version, tuple):
            version = '.'.join([str(x) for x in version])
        return version


setup(
    name='iso3166_1'
    description='ISO 3361-1 Country code package for Python',
    long_description=readme(),
    version=get_version(),
    url=
)
