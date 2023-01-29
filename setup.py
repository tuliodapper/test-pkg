"""Python setup.py for project_name package"""
import io
import os
from setuptools import find_packages, setup

project_name = 'test_pkg_2'
project_description = 'Testing package'
project_git = 'https://github.com/tuliodapper/test-pkg/'
project_author = 'Túlio Dapper'

def read(*paths, **kwargs):
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content

def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name=f"{project_name}",
    version=read(f"{project_name}", "VERSION"),
    description=f"{project_description}",
    url=f"{project_git}",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author=f"{project_author}",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [f"{project_name} = {project_name}.__main__:main"]
    },
)
