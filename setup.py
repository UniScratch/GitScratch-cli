from setuptools import setup

setup(
    name="GitScratch-cli",
    version="0.1",
    description="The command line interface for GitScratch",
    py_modules=["gitscratch_cli"],
    install_requires=[
        "click",
        "requests",
    ],
    entry_points='''
        [console_scripts]
        gitscratch_cli=gitscratch_cli:cli
    ''',
)
