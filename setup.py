import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="asp",
    version="0.0.1",
    author="Seyoung Park",
    author_email="seyoung.arts.park@protonmail.com",
    description="Aalto Audio Signal Processing Course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #scripts=['bin/perfect'],
    url="https://github.com/SuperShinyEyes/aalto-audio-signal-processing",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
    ]
)