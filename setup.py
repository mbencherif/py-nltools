from setuptools import setup

setup(
    name                 = 'py-nltools',
    version              = '0.1.3',
    description          = 'A collection of basic python modules for spoken natural language processing',
    long_description     = open('README.md').read(),
    author               = 'Guenter Bartsch',
    author_email         = 'guenter@zamia.org',
    maintainer           = 'Guenter Bartsch',
    maintainer_email     = 'guenter@zamia.org',
    url                  = 'https://github.com/gooofy/py-nltools',
    packages             = ['nltools'],
    install_requires     = [
                            'num2words', 'py-marytts', 'py-picotts', 'py-espeak-ng', 'pocketsphinx', 'py-kaldi-asr', 'numpy', 'webrtcvad', 'setproctitle'
                           ],
    classifiers          = [
                               'Operating System :: POSIX :: Linux',
                               'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                               'Programming Language :: Python :: 2',
                               'Programming Language :: Python :: 2.7',
                               'Programming Language :: Python :: 3',
                               'Programming Language :: Python :: 3.5',
                               'Intended Audience :: Developers',
                               'Topic :: Multimedia :: Sound/Audio :: Speech',
                               'Topic :: Scientific/Engineering :: Artificial Intelligence'
                           ],
    license              = 'LGPLv3',
    keywords             = 'natural language processing tokenizer nlp tts asr speech synthesis recognition',
    )

