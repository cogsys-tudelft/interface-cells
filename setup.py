from setuptools import setup

setup(
    extras_require={
        "test": ["pytest==7.4.3", "cocotb==1.8.1", "cocotb-test==0.2.4"]
    },
)
