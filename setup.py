from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="littlePrint",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tiny and convenient print utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/littlePrint",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "lprint=littlePrint.__main__:main",
        ],
    },
    keywords="print, utility, shortcut, python, debugging",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/littlePrint/issues",
        "Source": "https://github.com/yourusername/littlePrint",
        "Documentation": "https://github.com/yourusername/littlePrint#readme",
    },
)
