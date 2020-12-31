from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyrandmeme',
    version='0.0.6',
    description='Random memes for discord.py',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Poggy',
    author_email='email',
    License='MIT',
    classifiers=classifiers,
    keywords='memes',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'discord',
        'random2'
    ]
)
