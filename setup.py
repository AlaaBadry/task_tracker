from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in task_tracker/__init__.py
from task_tracker import __version__ as version

setup(
	name='task_tracker',
	version=version,
	description='A custom app to track tasks',
	author='xsolutions',
	author_email='alaabadry1@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
