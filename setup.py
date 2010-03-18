from distutils.core import setup
import sys

if sys.version < '2.6':
    print ''
    print '** json is required by embedly and comes standard with python version > 2.6'
    print ''
    sys.exit()

setup(name         = 'Embedly',
      description  = 'A simple OEMBED library to use with api.embed.ly',
      author       = 'Embed.ly, Inc.',
      author_email = 'developers@embed.ly',
      url          = 'http://api.embed.ly',
      version      = '0.1',
      py_modules   = ['embedly'],
      classifiers  = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: OEMBED',
        'Topic :: Software Development :: Libraries :: API',
      ],
     )
