from setuptools import setup

setup(
   name='getcoord',
   version='1.0',
   description='Search information of place',
   license='MIT',
   author='Efim Pechersky',
   author_email='pecherskii0404@gmail.com',
   url='https://github.com/EfimPechersky/firsttestlib',
   packages=['getcoord'], 
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)