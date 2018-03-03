from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='plottyprint',
      version='0.1',
      description='provide a couple of easy to use, very basic, printable plots on top of matplotlib',
      long_description=readme(),
      url='https://github.com/paultopia/plottyprint',
      classifiers=[
          'Development Status :: 3 - Alpha',
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3 :: Only"
      ],
      keywords="plotting, datavis",
      author='Paul Gowder',
      author_email='paul.gowder@gmail.com',
      license='MIT',
      packages=['plottyprint'],
      python_requires='>=3',
      install_requires=['numpy', 'matplotlib>=2.1.1', 'statsmodels', 'scipy'],
      zip_safe=False)
