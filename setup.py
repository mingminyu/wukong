from setuptools import setup, find_packages

VERSION = "0.0.7"

setup(
    name='wu5kong',
    version=VERSION,
    description='wu-kong package',
    platforms=["all"],
    license='GPL',
    author="yumingmin",
    author_email="yu_mingm623@163.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: System :: Monitoring",
        ],
    install_requires=[
        "rich>=12.0.0",
        "rich[jupyter]",
        "click==8.0.4",
        "requests>=2.25.1",
        "impyla>=0.17.0",
        "pandas>=1.3.1",
        "argcomplete==2.0.0",
        "pyppeteer==1.0.2",
        "pyppeteer_stealth==2.7.3",
        ],
    entry_points={
        "console_scripts": [
            "wk=wukong.__main__:main"
            ]
        }
    )
