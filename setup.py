from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    name="dsproject",
    version="0.0.1",
    author="khusnul2106",
    author_email="kkhusnul766@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)