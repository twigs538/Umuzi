from setuptools import setup, find_packages

setup(
    name='animals',
    version='1.0.0',
    decription='this package contain the animals class',
    author='Tshepiso Moloko',
    author_email='tmoloko538@gmail.com',
    url='https://github.com/Umuzi-org/Tshepiso-Moloko-224-animals-part-1-oop-basics-python',
    packages=find_packages(exclude=('tests*','testing*')),
    entry_points={
        'console_scripts': [
            'animals-cli = animals.animals:main',
        ],
    },
)