import setuptools

setuptools.setup(
    name='mdfind',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
