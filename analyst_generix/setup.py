from setuptools import setup, find_packages

setup(
    name="analyst_generix",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    install_requires=[
        "crewai>=0.11.0",
        "langchain>=0.1.0",
        "sqlalchemy>=2.0.0",
        "pymysql>=1.1.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.1",
        "openai>=1.3.0"
    ],
) 