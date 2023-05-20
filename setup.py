# setup.py placed at root directory
from setuptools import setup, find_packages
# import re

# __version__ = re.findall(
#     r""" __version__ =["']+([0-9\.\-dev]*)["']+""",
#     open('linkedinjobautomation/__init__.py').read(),
# )[0]

prod_requirements = []
dev_requirements = []

setup(
    name='python_challenges',
    version='1.0',
    author='umavenkatkaranam',
    description='python,algorithms, analytics',
    long_description='python exercises',
    url='',
    keywords='python ,setuptools',
    # packages='find:',
    packages=find_packages(),
    python_requires='>=3.7, <4',
    install_requires=['pandas', 'numpy', 'Scrapy',
                      'beautifulsoup4', 'pandas', 'seaborn', 'matplotlib',
                      'openpyxl'],
    extras_require={
        'test': ['pytest', 'coverage'],
    },
    package_data={
        'python_challenges': [],
    },
    entry_points={
        'console_scripts': [
            'python_challenges=python_challenges:autoapply',
        ]
    }
)
