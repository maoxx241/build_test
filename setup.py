from setuptools import setup, find_packages

setup(
    name="mindie_turbo",
    version="0.1.0",
    packages=find_packages(
        include=["mindie_turbo", "mindie_turbo.*"],
        exclude=["mindie_turbo.adapter", "mindie_turbo.adapter.*"],
    ),
)
