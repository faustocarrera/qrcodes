"""
QR Code generator and decoder
-----------------------------
A Python library for generating and decoding QR codes.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.1.0'
requirements = [
    'pillow>=11.3',
    'qrcode[pil]>=8.0',
    'pyzbar>=0.1.9'
]
with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()
   
config = {
    'name': 'qr_generator',
    'description': 'A Python library for generating and decoding QR codes',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'license': 'GPLv3+',
    'author': 'Fausto Carrera',
    'author_email': 'fausto.carrera@proton.me',
    'url': 'https://github.com/faustocarrera/qrcodes/',
    'download_url': 'https://github.com/faustocarrera/qrcodes/',
    'version': VERSION,
    'install_requires': requirements,
    'packages': ['qr_generator'],
    'include_package_data': True,
    'platforms': 'any',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)'
    ],
    'python_requires': '>=3.1'
}

setup(**config)
