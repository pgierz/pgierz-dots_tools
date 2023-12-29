from setuptools import setup

setup(
    name='gpg-subkey-generator',
    version='0.1.0',
    py_modules=['gpg_subkey_generator'],
    install_requires=[
        'python-gnupg',
        'questionary'
    ],
    entry_points='''
        [console_scripts]
        gpg-subkey-generator=gpg_subkey_generator:main
    ''',
    author='Paul Gierz',
    author_email='pgierz@mac.com',
    description='A tool to generate GPG subkeys interactively',
    keywords='GPG subkeys encryption signing authentication',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

