import setuptools

with open("README.md", "r") as fh:
    long_desc = fh.read()

setuptools.setup(
    name="sequences",
    version="0.0.8",
    author="Divyajeet Singh",
    author_email="knightt1821@gmail.com",
    description="provides the most famous of sequences of the OEIS",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url="https://github.com/divyajeettt/sequences",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)