from setuptools import setup, find_packages

import ast
import sys


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
    filename = 'iso3166/__init__.py'
    with open(filename, 'r') as f:
        tree = ast.parse(f.read(), filename)
        for node in tree.body:
            if (isinstance(node, ast.Assign) and
                    node.targets[0].id == '__version__'):
                version = ast.literal_eval(node.value)
        if isinstance(version, tuple):
            version = '.'.join([str(x) for x in version])
        return version


tests_require = [
    'pytest >= 2.7.0',
    'tox >= 2.1.1',
]


def get_install_requirements():
    install_requires = ['setuptools']
    if 'bdist_wheel' not in sys.argv and sys.version_info < (3, 4):
        install_requires.append('enum34')
    return install_requires


def get_extras_require():
    """Generate conditional requirements with environ marker."""
    for pyversion in '2.5', '2.6', '2.7', '3.2', '3.3':
        yield ':python_version==' + repr(pyversion), ['enum34']


setup(
    name='iso-3166-1',
    version=get_version(),
    description='ISO 3361-1 Country code package for Python',
    long_description=readme(),
    license='Public Domain',
    author='Kang Hyojun',
    author_email='ed' '@' 'spoqa.com',
    packages=find_packages(),
    package_data={'iso3166': ['table.csv']},
    url='http://github.com/spoqa/iso-3166-1',
    keywords='internationalization i18n country iso3166',
    install_requires=get_install_requirements(),
    extras_require=dict(
        get_extras_require(),
        tests=tests_require
    ),
    tests_require=tests_require,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Software Development :: Internationalization',
    ]
)
