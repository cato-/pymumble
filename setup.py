from setuptools import setup
import os

try:
    reqs = open(os.path.join(os.path.dirname(__file__),'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(name='pymumble',
      version="1.0",
      description='Python library acting as client to mumble server',
      long_description="",
      author='Robert Hendrickx',
      author_email='rober@percu.be',
      url='https://github.com/Robert904/pymumble',
      packages=['pymumble'],
      include_package_data=True,
      classifiers=[
          ],
      )
