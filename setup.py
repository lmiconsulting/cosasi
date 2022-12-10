from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="cosasi",
    version="0.0.4",
    author="Lucas H. McCabe",
    author_email="lmccabe@lmi.org",
    description="COntagion Simulation And Source Identification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lmiconsulting/cosasi",
    packages=find_packages(),
    package_data={"cosasi": ["source_inference/algorithm_details.json"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
