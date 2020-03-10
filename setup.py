import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='trellis',
    version='0.0.1',
    author='Michael Davies',
    author_email='michael@the-davies.net',
    description='A CLI for trello',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mrda/trellis',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
        'trellis = trellis.trellis:main'
        ],
    },
)
