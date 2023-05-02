from setuptools import find_packages, setup

setup(
    name='whitetower',
    packages=find_packages(),
    version='0.1',
    description='Whitetower the smart docker-compose stack updater',
    author='Alexander Tsidaev',
    license='MIT',
    requires=["boto3", "yaml"]
)