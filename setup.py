import setuptools

with open("README.md", "r") as f:
    readme = f.read()

setuptools.setup(
    name="themepy",
    version ="0.2.0",
    author ="Peter McKeever",
    author_email ="hello@petermckeever.com",
    description ="a tools suite to manage themes in matplotlib",
    long_description=readme,
    long_description_content_type="text/markdown",
    url ="https://github.com/petermckeeverPerform/themepy",
    packages=setuptools.find_packages(),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        "": ["*.txt"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Framework :: Matplotlib"
    ],
    python_requires='>=3.7',
)