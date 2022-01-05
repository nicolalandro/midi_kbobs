[![download counts on pypi](https://img.shields.io/pypi/dm/midiknobs.svg)](https://pypistats.org/packages/midiknobs)

# midi_kbobs

This project is a gui able to set a midi knobs as controller of Linux master audio.

# User Doc

* install:
```
sudo apt-get install python3-dev
# on OpenSuse: sudo zypper in python3-devel
# on Other dist: https://stackoverflow.com/questions/21530577/fatal-error-python-h-no-such-file-or-directory#21530768
python3 -m pip install midiknobs
```
* run:

```bash
python3 -m midiknobs
```

![Gui image](https://raw.githubusercontent.com/nicolalandro/midi_kbobs/master/imgs/gui.png)

* Select the Midi device
* Set the correct value of "Channel" and "Control"
* Click "Connect"
* Move your midi knob
* Click "Disconnect"

# Dev Doc

```bash
# use python>=3.5
python setup.py install
midiknobs_gui
```
