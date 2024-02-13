from setuptools import find_packages, setup

__REQUIREMENTS__ = ["check"]


def read_requirements(req_path):
    with open(req_path) as f:
        return f.read().splitlines()


if __name__ == "__main__":
    requirements = dict()
    for req in __REQUIREMENTS__:
        requirements[req] = read_requirements(f"requirements/{req}.txt")

    setup(
        name="stringutils",
        version="0.1.0",
        packages=find_packages(exclude=["tests"]),
        install_requires=requirements["check"],
        python_requires=">=3.8",
        tests_require=["pytest"],
        setup_requires=["pytest-runner"],
    )
