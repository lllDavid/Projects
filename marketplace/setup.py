from setuptools import setup, find_packages

def get_requirements(filename) -> list[str]:
    with open(filename, 'r', encoding='utf-8-sig') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

setup(
    name="Marketplace",
    version="1.0.0",
    author="lllDavid",
    description="Crypto Marketplace",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
    'marketplace-cli=marketplace.run:Main',
        ],
    },
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lllDavid/marketplace",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    install_requires=get_requirements('requirements.txt'),
    python_requires=">=3.12",
    keywords="flask mariadb crypto marketplace",
)
