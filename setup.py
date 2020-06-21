
from setuptools import setup, find_packages
import pcalender
requirements_path='requirements.txt'

def parse_requirements(filename):
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

install_reqs = parse_requirements(requirements_path)
setup(
    name='pcalender',
    version=str(pcalender.__version__),
    description=pcalender.__description__,
    author=pcalender.__author__,
    author_email=pcalender.__email__,
    license='MIT',
    install_requires=parse_requirements(requirements_path) ,
    packages=find_packages(),
      )