from setuptools import setup, find_packages

setup(
    name='person',
    version='1.0.0',
    decription='this package contain the person function',
    author='Tshepiso Moloko',
    author_email='tmoloko538@gmail.com',
    url='https://github.com/Umuzi-org/Tshepiso-Moloko-223-person-python',
    packages=find_packages(exclude=('tests*','testing*')),
    entry_points={
        'console_scripts': [
            'person-cli = person.person:main',
        ],
    },
)