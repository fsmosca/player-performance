import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name="player-performance",
    version='0.3.0',
    author='Ferdinand Mosca',
    author_email="ferdymosca@gmail.com",
    description="Gets the player performance and rating change from the tournament.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fsmosca/player-performance",
    project_urls={
        "Bug Tracker": "https://github.com/fsmosca/player-performance/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
          'chess==1.9.1',
          'pandas'
    ],
    entry_points={
        'console_scripts': [
            'performance = performance:main',
        ]
    }
)