BorderlessStone
===============

A Python script that forces Hearthstone to play in Borderless Window in any resolution you want

A Little Preview
----------------

![Screenshot](https://raw.github.com/NullScope/BorderlessStone/master/capture.gif)


How to use
==========

You can choose between the script and the compiled executable binaries available [here](https://sourceforge.net/projects/borderlessstone/files/)

For the script you will need to install python and other dependencies in order to run it (Make sure to have python in your PATH)

Create a .bat file in the same folder with the following:

```
python BorderlessStone.py -w <YOUR SCREEN WIDTH> -h <YOUR SCREEN HEIGHT>
```

Example:

```
python BorderlessStone.py -w 1366 -h 768
```

For the binaries, also have a batch file with the following:

```
start BorderlessStone.exe -w <YOUR SCREEN WIDTH> -h <YOUR SCREEN HEIGHT>
```

Commands
========

Currently, there are only 2 straight foward commands:


`--width` sets Hearthstone Window Width

`--height` sets Hearthstone Window Height


Dependencies
============

The software required to be installed in your computer to run the Python script (not the binaries) are:

* Python 2.7.6
* Pywin32 Build 218

To compile to a binary executable, you will need PyInstaller 2.1
