from setuptools import setup, find_packages

# Function to read requirements.txt and return a list of dependencies
def read_requirements(file_path):
    """Reads a requirements file and returns a list of requirements."""
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="Office_toolbox",
    version="1.02",
    author="Karthick Jayaraman",
    description="A useful set of tools for office productivity",
    url="https://github.com/Karthick-840/Office_Toolbox",
    py_modules=["Directory_Tools","Git_Tools","Kaggle_Tools","PDF_Tools","API_Tools","String_Ops","Time_Ops"],  # List the module directly
    install_requires=find_packages(),  # Read requirements from requirements.txt
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)