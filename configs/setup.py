import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uber-lyft-price-prediction",
    version="1.0.0",
    author=["Bhushan Mahajan", "Anurag Pawar", "Mohit Patil"],
    author_email="bhushanmahajan707@gmail.com",
    description="A web application for predicting dynamic price of Uber and Lyft cabs depending on various parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BhushanMahajan25/uber-lyft-price-prediction",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                      "tests.*", "tests"]),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)