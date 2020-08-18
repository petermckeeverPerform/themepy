import setuptools

setuptools.setup(
    name="themepy",
    version = "0.0.4",
    author = "Peter McKeever",
    author_email = "hello@petermckeever.com",
    description = "a tools suite to manage themes in matplotlib",
    url = "https://github.com/petermckeeverPerform/themepy",
    packages=setuptools.find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.7',
)