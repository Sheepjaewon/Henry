from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # 의존하는 패키지가 있다면 여기에 추가
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='Description of my library',
    url='https://github.com/yourusername/mylibrary',
)
