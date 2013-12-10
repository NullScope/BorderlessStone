BorderlessStone
===============

A Python script that forces Hearthstone to play in Borderless Window in any resolution you want

A Little Preview
----------------

![Screenshot](https://raw.github.com/NullScope/BorderlessStone/master/capture.gif)


How to use
==========

You can choose between the script and the compiled executable binaries available [here](https://sourceforge.net/projects/borderlessstone/files/) (Rename the file you download to BorderlessStone for easier guide following)

For the script you will need to install python and other dependencies in order to run it


Create a .bat file in the same folder with the following:

```
python BorderlessStone.py -w <YOUR SCREEN WIDTH> -h <YOUR SCREEN HEIGHT>
```

Example:

```
python BorderlessStone.py -w 1366 -h 768
```

If using the binaries, instead have a batch file with the following:

```
start BorderlessStone.exe -w <YOUR SCREEN WIDTH> -h <YOUR SCREEN HEIGHT>
```

The default behaviour of the script (without any command line) will remove the borders and use the game's current resolution (**NOT** recommended as it's still somewhat buggy)

##### Do not use a higher resolution than your monitor is capable of, this will prevent the script from removing the borders

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

Current Known Issues
--------------------

* If you see the game slightly stretched out like [this](http://i.imgur.com/Fjq41HN.png), don't panic, this only sometimes happens when the resolution is changed from a lower value to fullscreen, restarting hearthstone and running the script again will fix it
