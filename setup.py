from setuptools import setup, find_packages

setup(
    name='dregni',
    version='0.0.1',
    description='A basic event management application for Django',
    author='Marty Alchin',
    author_email='marty@martyalchin.com',
    url='http://code.google.com/p/dregni/',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
