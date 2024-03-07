import os

from setuptools import find_packages, setup

__REQUIREMENTS__ = ["base", "check"]
__PACKAGE_NAME__ = "pytholic-stringutils"
__VERSION__ = "0.1.3"


def read_requirements(req_path):
    with open(req_path) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    requirements = {}
    for req in __REQUIREMENTS__:
        req_path = f"requirements/{req}.txt"
        print(req_path)
        if not os.path.exists(req_path):
            raise FileNotFoundError(f"File not found: {req_path}")
        requirements[req] = read_requirements(req_path)

    setup(
        name=__PACKAGE_NAME__,
        version=__VERSION__,
        packages=find_packages(exclude=["tests", "README.md"]),
        install_requires=requirements["base"],
        python_requires=">=3.8",
        tests_require=requirements["check"],
        setup_requires=["pytest-runner"],
        long_description=open("README_PACKAGE.md").read(),
        long_description_content_type="text/markdown",
    )
