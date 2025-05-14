from setuptools import setup, find_namespace_packages

setup(
    name="resume-generator",
    version="0.1",
    packages=find_namespace_packages(include=['src.*', '*']),
    package_dir={
        '': '.',  # Root package can be imported from root directory
        'resume_generator': 'src'  # Package modules are in src/
    },
    install_requires=[
        "anthropic>=0.51.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
    },
    author="Alessandro De La Garza",
    author_email="aless.delagarza@gmail.com",
    description="AI-powered resume generator that creates tailored resumes",
    python_requires=">=3.8",
)