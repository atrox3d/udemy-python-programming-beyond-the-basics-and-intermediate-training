import setuptools

setuptools.setup(
    name='mypackage',
    version='0.1',
    description='testing the installation package',
    url='#',
    author='author',
    author_email='',
    license='',
    packages=['mypackage'],
    # packages=setuptools.find_packages(),
    zip_safe=False
)

# pip install . from parent directory
# https://stackoverflow.com/a/42541684

"""
DEPRECATION: mypackage is being installed using the legacy 'setup.py install' method, 
because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. 
pip 23.1 will enforce this behaviour change. 
A possible replacement is to enable the '--use-pep517' option. 
Discussion can be found at https://github.com/pypa/pip/issues/8559
"""
