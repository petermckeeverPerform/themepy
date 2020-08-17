import setuptools

setuptools.setup(
    name="themepy",
    version = "0.0.1",
    author = "Peter McKeever",
    author_email = "",
    description = "a tools suite to manage themes in matplotlib",
    url = "",
    packages=setuptools.find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt"]},
    classifiers=[
        "Programming Language :: Python 3",
    ],
    python_requires='>=3.7,
)