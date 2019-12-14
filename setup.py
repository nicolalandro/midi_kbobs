from setuptools import setup, find_packages

setup(
    name="midiknobs",
    description="A small pyqt5 gui to use midi knobs for change linux master audio",
    version="0.0.1",
    python_requires='>=3.5',
    install_requires=["python-rtmidi", "mido", "vext.pyqt5", "PyQt5"],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['midiknobs_gui=midiknobs.__main__:main'],
    },
)
