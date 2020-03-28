"""Packaging for demo CLI."""
from setuptools import find_packages, setup
from demo.version import version


def version():
    """Return current package version."""
    with open("demo/version/A-major", "rt") as f:
        major = f.read().replace("\n", "")
    with open("demo/version/B-minor", "rt") as f:
        minor = f.read().replace("\n", "")
    with open("demo/version/C-patch", "rt") as f:
        patch = f.read().replace("\n", "")

    return "{}.{}.{}".format(major, minor, patch)


setup(
    name="demo",
    description="demo CLI tool",
    url="http://docs.example.com",
    author="Mislav Cimpersak",
    license="MIT",
    version=version(),
    packages=find_packages(exclude=["tests"]),
    install_requires=["Click>=7.0", "requests>=2.19.1", "boto3>=1.9.188",],
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-mock"],
    entry_points="""
        [console_scripts]
        demo=demo.cli:cli
    """,
    package_data={"demo": ["version/*"]},
)
