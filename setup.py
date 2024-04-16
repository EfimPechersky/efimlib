from setuptools import setup

setup(
   name='getcoord',
   version='1.0',
   description='Search information of place',
   license='MIT',
   author='Efim Pechersky',
   author_email='pecherskii0404@gmail.com',
   url='https://github.com/EfimPechersky/getcoord',
   packages=['getcoord'], 
   install_requires=['git+https://github.com/pandas-dev/pandas#egg=pandas'], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
