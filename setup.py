from setuptools import setup, find_packages

setup(
    name="midi_knobs",
    version="0.0.1",
    install_requires=["python-rtmidi", "mido", "vext.pyqt5"],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['midi_knobs=midi_knobs.__main__:main'],
    }
)

