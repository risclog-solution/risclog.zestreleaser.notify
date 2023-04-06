#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as history_file:
    history = history_file.read()

setup(
    author='riscLOG Solution GmbH',
    author_email='info@risclog.de',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: German',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description='Notify about new release in keybase channel.',
    install_requires=[
        'pydantic[dotenv]',
        # Add your dependencies here
    ],
    extras_require={
        'docs': [
            'Sphinx',
        ],
        'test': [
            'pytest-cache',
            'pytest-cov',
            'pytest-flake8',
            'pytest-rerunfailures',
            'pytest-sugar',
            'pytest',
            'coverage',
            # https://github.com/PyCQA/flake8/issues/1419#issuecomment-947243876
            'flake8<4',
            'mock',
            'requests',
        ],
    },
    license='MIT license',
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='risclog.zestreleaser.keybase',
    name='risclog.zestreleaser.keybase',
    packages=find_packages('src'),
    namespace_packages=['risclog'],
    package_dir={'': 'src'},
    url='https://github.com/risclog-solution/risclog.zestreleaser.keybase',
    version='0.1.0.dev0',
    zip_safe=False,
)