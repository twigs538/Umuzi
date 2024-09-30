from setuptools import setup, find_packages

setup(
    name='password_checker',
    version='1.0.0',
    decription='this package contain the password checker',
    author='Tshepiso Moloko',
    author_email='tmoloko538@gmail.com',
    url='https://github.com/Umuzi-org/Tshepiso-Moloko-269-password-checker-python',
    packages=find_packages(exclude=('tests*','testing*')),
    entry_points={
        'console_scripts': [
            'password_checker-cli = password_checker.password_checker:main',
        ],
    },
)