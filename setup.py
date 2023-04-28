from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bureau/__init__.py
from bureau import __version__ as version

setup(
	name="bureau",
	version=version,
	description="Money Dashboard App",
	author="Momodou khan",
	author_email="khanmomodou11@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
