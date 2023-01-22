from setuptools import setup, find_packages

setup(
    name='homework_exercise',
    version='0.0.1',
    install_requires=[
        'numpy'
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={'homework_exercise':['*.json','*.toml']},
    include_package_data=True
)