from __future__ import print_function
from setuptools import setup, find_packages
import io
import codecs
import os
import sys

#from setuptools.command.test import test as TestCommand

# class PyTest(TestCommand):
#     def finalize_options(self):
#         TestCommand.finalize_options(self)
#         self.test_args = []
#         self.test_suite = True

#     def run_tests(self):
#         import pytest
#         errcode = pytest.main(self.test_args)
#         sys.exit(errcode)



here = os.path.abspath(os.path.dirname(__file__))

def readme(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = readme('README.rst', 'CHANGES.rst')


setup(
    name='MyPackage1',
      version='0.1',
      description='Test Package1',
      long_description=readme(),
      classifiers=[
       'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      ],
      keywords='module, package, test',
      url='http://github.com/muratcabuk',
      author='Murat Cabuk',
      author_email='mcabuk@gmail.com',
      license='MIT',
      packages=['Package1'],
      include_package_data=True,
      platforms='any',
      #test_suite='sandman.test.test_sandman',
      install_requires=[
          'matplotlib', 'numpy'
      ],
      extras_require={
        'testing': ['pytest'],
    }
)



