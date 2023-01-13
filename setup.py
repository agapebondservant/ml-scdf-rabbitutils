from setuptools import setup, find_packages

setup(
    name='scdfrabbitutils',
    version='2.0',
    packages=find_packages(),
    install_requires=[
        'pika',
        'streamlit==1.12.0'
    ]
)
