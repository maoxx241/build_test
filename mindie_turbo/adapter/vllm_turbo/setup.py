from setuptools import setup, find_packages

setup(
    name="vllm_turbo",
    version="0.1.0",
    packages=find_packages(include=["vllm_turbo", "vllm_turbo.*"]),
    install_requires=["mindie_turbo"],
)
