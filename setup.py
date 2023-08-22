import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text_Summerizer_Project"
AUTHOR_USER_NAME = "themeynoush"
SRC_REPO = "Text_Summerizer"
AUTHOR_EMAIL = "themeynoush@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summerizer as an NLP project.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)




# from setuptools import find_packages, setup
# from typing import List


# def get_requirements(file_path: str) -> List[str]:
#     '''
#     This function will return the list of requirements, excluding -e lines.
#     '''
#     requirements = []
#     with open(file_path) as file_obj:
#         for line in file_obj:
#             line = line.strip()
#             if not line.startswith('-e'):
#                 requirements.append(line)

#     return requirements


# setup(
#     name='Deezer_Music_Consumption_Analysis',
#     version='0.0.1',
#     author='Zohreh (Meynoush) KOHANDANI',
#     author_email='themeynoush@gmail.com',
#     packages=find_packages(),
#     # use get_requirements function for getting the requirements from requirements.txt
#     install_requires=get_requirements('requirements.txt')
# )