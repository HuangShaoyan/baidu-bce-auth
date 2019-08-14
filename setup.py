# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages, setup

from bceauth import __version__


def read_requires():
    reqs = []
    with Path('requirements.txt').open(encoding='utf-8') as f:
        for line in f.read().splitlines():
            line = line.strip()
            if len(line) > 0 and not line.startswith(('#', '--')):
                reqs.append(line)
    return reqs


def read_long_description():
    return Path('README.md').read_text(encoding='utf-8')


setup(
    name='baidu-bce-auth',
    version=__version__,
    author='huangshaoyan',
    author_email='huangshaoyan1982@gmail.com',
    long_description=read_long_description(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=read_requires(),
    tests_require=[],
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    url='https://github.com/HuangShaoyan/baidu-bce-auth',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Typing :: Typed',
    ],
)
