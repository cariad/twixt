from pathlib import Path

from setuptools import setup

from twixt import get_version

version = get_version()

readme_path = Path(__file__).parent / "README.md"

with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.11",
    "Typing :: Typed",
]

if "a" in version:
    classifiers.append("Development Status :: 3 - Alpha")
elif "b" in version:
    classifiers.append("Development Status :: 4 - Beta")
else:
    classifiers.append("Development Status :: 5 - Production/Stable")

classifiers.sort()

setup(
    author="Cariad Eccleston",
    author_email="cariad@cariad.earth",
    classifiers=classifiers,
    description="Betwixt two values",
    include_package_data=True,
    install_requires=[
        "bendy==1.0.0a6",
    ],
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="twixt",
    packages=[
        "twixt",
    ],
    package_data={
        "twixt": ["py.typed"],
    },
    python_requires=">=3.11",
    url="https://github.com/cariad/twixt",
    version=version,
)
