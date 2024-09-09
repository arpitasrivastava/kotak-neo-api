from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.0"
# To install the library, run the following
#
# python setup.py install

REQUIRES = ['bidict==0.22.1', 'certifi', 'idna', 'numpy', 'pyjsparser==2.7.1', 'PyJWT==2.6.0',
            'python-dateutil==2.8.2', 'python-dotenv==1.0.0', 'requests', 'six==1.16.0', 'urllib3',
            'websocket-client==1.5.1', 'websockets', 'pandas', 'asyncio==3.4.3']

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API",
    author="ne API",
    author_email="",
    url="",
    keywords=["Neo-Trade API", "Neo Trade API's"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    """
)
