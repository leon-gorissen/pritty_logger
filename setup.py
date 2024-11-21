from setuptools import setup, find_packages

setup(
    name="pritty_logger",
    version="0.3.0",
    description="A logger with rich formatting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Leon Gorißen",
    author_email="leon.gorissen@gmx.de",
    url="https://github.com/leon-gorissen/pritty_logger",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
