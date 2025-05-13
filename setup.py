from setuptools import setup, find_packages

setup(
    name="resume-generator",
    version="0.1.0",
    packages=find_packages(),
    package_dir={"": "src"},
    install_requires=[
        # Add your dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "isort>=5.0",
            "flake8>=6.0",
        ],
    },
    author="Alessandro De La Garza",
    author_email="aless.delagarza@gmail.com",
    description="An AI-powered resume generator that creates tailored resumes for job applications",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    keywords="resume, cv, ai, generator",
    url="https://github.com/alessdelagarza/resume-generator",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
) 