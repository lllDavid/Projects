from setuptools import setup, find_packages

setup(
    name="your_project_name",  # Replace with your project name
    version="0.1.0",  # Initial version number
    packages=find_packages(),  # Automatically find all packages in your project
    include_package_data=True,  # Include non-Python files (e.g., static, templates)
    install_requires=[
        "Flask>=3.0.3",
        "mariadb>=1.1.2",
    ],  # List of dependencies (these will be installed with pip)
    entry_points={
        'console_scripts': [
            'your_project_name=your_project_name.cli:main',  # If your project has command-line scripts
        ],
    },
    # Optional fields:
    author="Your Name",
    author_email="your_email@example.com",
    description="A short description of your project",
    long_description=open('README.md').read(),  # Optional, but helpful to add long description from README
    long_description_content_type="text/markdown",  # If you're using markdown for the README
    url="https://github.com/your_username/your_project",  # Replace with your project URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12.8",  # Required Python version
    keywords="flask mariadb marketplace",  # Optional keywords
)
