from setuptools import setup, find_packages
import sys

if sys.version_info.major != 3:
    print('This Python is only compatible with Python 3, but you are running '
          'Python {}. The installation will likely fail.'.format(sys.version_info.major))


setup(name='rl',
      packages=[package for package in find_packages()
                if package.startswith('rl')],
      install_requires=[
      ],
      description='RL algorithms in PyTorch',
      author='',
      url='https://github.com/VengeurK/pytorch-a2c-ppo-acktr',
      author_email='',
      version='1.0')
