import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

with open("LICENSE.txt", "r", encoding = "utf-8") as fl:
    long_description_license = fl.read()

setuptools.setup(
    name = "ConvAA2lig",
    version = "0.0.1",
    author = "Moonipur",
    author_email = "moo_sutthittha@hotmail.com",
    description = "The ConvAA2lig is a simple convert PDB file from Amino acid name to your Ligand name.",
    long_description = long_description and long_description_license,
    long_description_content_type = "text/markdown",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = "<=3.10"
)