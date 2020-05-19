from setuptools import setup, find_packages

setup(
    version="1.0",
    name="noisepy",
    packages=find_packages(),
    python_requires=">=3",
    install_requires=[
        "numpy",
        "scipy",
        "numba",
        "obspy",
        "pandas",
        "pyasdf",
        "pycwt",
        "matplotlib",
        "mpi4py",
        "markdown",
    ],
    author="Chengxin Jiang & Marine Denolle",
    author_email="chengxin_jiang@fas.harvard.edu & mdenolle@fas.harvard.edu",
    description="A High-performance Computing Python Package for Ambient Noise Analysis",
    license="MIT license",
    url="https://github.com/mdenolle/NoisePy",
    keywords="ambient noise, cross-correlation, seismic monitoring, velocity change "
    " surface wave dispersion",
    platforms=["any"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    scripts=["scripts/*.py"],
)
