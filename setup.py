from setuptools import setup, find_packages
import os

def read(*names):
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, *names)
    return open(path, 'r').read().strip()

version = read('Products', 'PloneBooking', 'version.txt')

setup(
    name='Products.PloneBooking',
    version=version,
    description="A booking center for Plone",
    long_description=(
        read("Products", "PloneBooking", "README.txt") +
        "\n\n" +
        read("docs", "CHANGES.txt")
        ),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 3.3",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='plone zope booking',
    author='Alter Way Solutions',
    author_email='support@alterway.fr',
    url='http://alterway.fr',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """
    )
