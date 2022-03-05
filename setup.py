
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

    name='svhnl',

    version='0.0.2',

    description='SVHN dataset preprocessing and annotation file reading and converting python library',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/ACRA-FL/svhnL.git',

    author='nipdep',

    author_email='nipun1deelaka@gmail.com',

    classifiers=[  # Optional

        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],


    keywords='sample, setuptools, development',

    packages=['svhnl'],

    python_requires='>=3.5, <4',

    install_requires=['numpy', 'pandas', 'matplotlib', 'opencv-python'],

    extras_require={
        'dev': ['check-manifest',
                'pytest>=3.7'],
        'test': ['coverage', 'unittest'],
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/ACRA-FL/svhnL/issues',
        'Source': 'https://github.com/ACRA-FL/svhnL/',
    },
)
