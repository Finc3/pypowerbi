from setuptools import setup

setup(name='pypowerbi',
      version='0.27',
      description='A python library for Microsoft\'s PowerBI',
      url='http://github.com/Enalytics/pypowerbi',
      author='Chris Berry',
      author_email='chris@chrisberry.com.au',
      license='MIT',
      packages=['pypowerbi'],
      install_requires=[
            'requests',
            'msal',
            'future-fstrings',
      ],
      zip_safe=False)
