from setuptools import setup
import ai_obj

DESCRIPTION = "AI-Obj mapper"
NAME = 'ai_obj'
AUTHOR = 'knaou'
AUTHOR_EMAIL = 'monaou@gmail.com'
URL = 'https://github.com/knaou'
LICENSE = 'BSD 3-Clause License'
DOWNLOAD_URL = 'https://github.com/knaou/ai_obj'
VERSION = ai_obj.__version__
PYTHON_REQUIRES = ">=3.11"

INSTALL_REQUIRES = [
    'openai>=1.46.0',
]

EXTRAS_REQUIRE = {
}

PACKAGES = [
    'ao_obj'
]

CLASSIFIERS = [
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
]

# with open('README.rst', 'r') as fp:
#     readme = fp.read()
# with open('CONTACT.txt', 'r') as fp:
#     contacts = fp.read()
# long_description = readme + '\n\n' + contacts
long_description = ""

setup(name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=PACKAGES,
    classifiers=CLASSIFIERS
)
