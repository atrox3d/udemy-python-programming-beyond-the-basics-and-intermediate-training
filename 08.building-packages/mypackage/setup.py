import setuptools

setuptools.setup(
    name='mypackage',
    version='0.1',
    description='testing the installation package',
    url='#',
    author='author',
    author_email='',
    license='',
    # packages=['mypackage'],
    packages=setuptools.find_packages(),
    zip_safe=False
)

# pip install . from parent directory
