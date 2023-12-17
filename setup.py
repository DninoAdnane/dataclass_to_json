import os

from setuptools import find_packages, setup

about = {}
base = os.path.abspath(os.path.dirname(__file__))
with open(
    os.path.join(base, "src", "dataclass_to_json", "__version__.py"), "r"
) as f:
    exec(f.read(), about)

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    packages=find_packages("src"),
    package_data={"": ["LICENSE"]},
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.7",
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries",
    ],
    project_urls={
        "Source": "https://github.com/DninoAdnane/dataclass_to_json",
    },
)
