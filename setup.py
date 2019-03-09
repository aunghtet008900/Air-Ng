#-*- coding: utf-8 -*-
import os
from setuptools import setup
if os.path.exists('README.md'):
   with open('README.md') as desc:
        long_desc = desc.read()


setup(
    name='Air_Ng',
    version='1.0',
    description='Reconnaisance,Information-Gathering,FootPrinting',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='JaxBCD',
    author_email='oke.wae906@gmail.com',
    license='apache 2.0',
    url='https://github.com/jaxBCD/Air-Ng',
    keywords='Information Gathering',
    classifiers=[
                 'Development Status :: 3 - Alpha', 
                 'License :: OSI Approved :: MIT License', 
                 'Programming Language :: Python', 
                 'Programming Language :: Python :: 3.3', 
                 'Programming Language :: Python :: 3.4', 
                 'Programming Language :: Python :: 3.5', 
                 'Programming Language :: Python :: 3.6', 
                 'Programming Language :: Python :: 3.7', 
                 'Natural Language :: English', 
                 'Topic :: System :: Networking :: Monitoring :: Hardware Watchdog'
                 ],
    packages=['Air_Ng'],
    install_requires=['requests','python-whois'],
    include_package_data=True,
    zip_safe=False
)
