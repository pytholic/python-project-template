from setuptools import find_packages, setup

__REQUIREMENTS__ = ["base", "check"]
__PACKAGE_NAME__ = "stringutils"
__VERSION__ = "0.1.0"


def read_requirements(req_path):
    with open(req_path) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    requirements = {}
    for req in __REQUIREMENTS__:
        requirements[req] = read_requirements(f"requirements/{req}.txt")

    setup(
        name=__PACKAGE_NAME__,
        version=__VERSION__,
        packages=find_packages(exclude=["tests"]),
        install_requires=requirements["base"],
        python_requires=">=3.8",
        tests_require=requirements["check"],
        setup_requires=["pytest-runner"],
    )
