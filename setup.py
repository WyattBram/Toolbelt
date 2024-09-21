from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name = 'toolbelt',
    version = '0.1.1',
    author = 'Wyatt Bramblett',
    author_email = 'wbramblett1@gmail.com',
    license = 'MIT',
    description = 'Cache commonly used commands',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = '',
    py_modules = ['commands','toolbelt'],
    packages = find_packages(),
    install_requires = ["click>=7.1.2"],
    python_requires='>=3.7',
    entry_points = '''
        [console_scripts]
        toolbelt=toolbelt:cli
    '''
)
