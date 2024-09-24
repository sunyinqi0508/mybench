from setuptools import setup, find_packages

setup(
    name= 'mybench',  # Name of your library
    version= '0.1.0',    # Initial version
    description= 'Show execution time for prompt.',
    author='Yinqi Sun',
    author_email='s@syq.su',
    packages=find_packages(),  # Automatically finds packages in the directory
    install_requires=[],  # List of dependencies
)
