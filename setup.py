from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longdesc = f.read()
    
setup(
  name='scratchBot',
  description='A bot in the works that offers some simple commands for profile pages',
  long_description=longdesc,
  url='https://github.com/Snipet/scratchBot',
  license='MIT',
  keywords='scratch bot commands'
  classifiers=[
    'Natural Language :: English',
    'Programming Language :: Python :: 3 :: Only',
		'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License'
    ],
  packages=find_packages()
  install_requires=[
    'requests',
    'scratchapi2'
    ],
  python_requires='>=3.5'
  )
