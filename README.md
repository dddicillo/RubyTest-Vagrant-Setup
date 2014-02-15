RubyTest-Vagrant-Setup
======================

## Overview
A script used to quickly setup the RubyTest plugin to work with Rails projects running on Vagrant. This allows the user to run RubyTest on their host machine. This is especially useful due to the fact that the way RubyTest is setup currently requires the user to adjust the settings whenever changing project directories. This script can also be useful to those attempting to set up RubyTest to run within Vagrant for the first time.

## Installation/Setup
- Open `config.ini`
- Adjust the settings accordingly

## Usage
- Run `testenv.py` from the command line
```bash
$ python testenv.py [project_dir]
```

## Contact
dddicillo@gmail.com