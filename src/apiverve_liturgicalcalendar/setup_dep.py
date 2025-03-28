from setuptools import setup, find_packages

setup(
    name='apiverve_liturgicalcalendar',
    version='1.1.9',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'setuptools'
    ],
    description='Liturgical Calendar is a simple tool for getting the dates of the Liturgical Calendar. It returns the dates of the Liturgical Calendar for a given year.',
    author='APIVerve',
    author_email='hello@apiverve.com',
    url='https://apiverve.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
