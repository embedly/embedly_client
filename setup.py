from distutils.core import setup
import sys

if sys.version < '2.6':
    try:
        import simplejson
    except:
        print ''
        print '** simplejson is required by embedly to perform json decoding'
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
