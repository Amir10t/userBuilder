from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["mysql.connector>=2.2.9"]

setup(
    name="userbuilder",
    version="0.0.1",
    author="Amir Talebi",
    author_email="amirhasantalebi1401@yahoo.com",
    description="",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Amir10t/UserBuilder",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.11.4",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)