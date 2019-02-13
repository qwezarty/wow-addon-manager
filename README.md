# WOW Addon Manager

*A **cli tool** for maintaining **World of Warcraft** addons. Built with python3.7.*

[![Build Status](https://travis-ci.org/qwezarty/wow-addon-manager.svg?branch=master)]( https://travis-ci.org/qwezarty/wow-addon-manager.svg?branch=master)
[![切换中文](https://img.shields.io/badge/README-%20切换中文-yellow.svg)](README_zh.md)

## Project status

Just finish search && install at 12.Feb! I'm trying to release v1.0 before March! 

| Task                      | Status                           |
|:--------------------------|:--------------------------------:|
| scaffolds && cli entrance |                            Done! |
| system && user configs    |                            Done! |
| module: info              |                            Done! |
| module: install           |                            Done! |
| module: search            |      in-progress, planned 14 Feb |
| module: update            |      in-progress, planned 16 Feb |
| module: remove            |      not started, planned 18 Feb |
| module: upgrade           |       not started, planed 21 Feb |
| module: scan              |      not started, planned 25 Feb |
| release v1.0              |             planned before March |

## Important

The purpose to build *wow-addon-manager* at the very beginning is to make an alternative **cli tool** to *Curse Client (integrate with Twich now, I don't like this)*.

This project is now in **early stage of development**. There's no stable release at all!

Now here is what you want if you're a *wower && developer*.

I'm enthusiastically hope you can join me and make any improvements or suggestions to it.

## Features will be supported

- source: curseforge(in progress), wowinterface(planned)

- search/detail/install/update/remove addons(in progress)

- check if there're addons outdated and update them all(planned)

- local addons auto detected(planned)

- windows-10 && macOS will both be full supported at release v1.0

## Setup notes

To clone and run the code, **Python 3 (with pip)** and **Git** should be installed.

You can run these command lines below on Mac/Linux *after install python 3 & git*:

``` bash
# clone this repository
git clone https://github.com/qwezarty/wow-addon-manager.git
# go into the repository
cd wow-addon-manager
# install dependencies(or using 'sudo' prefix if permission denied)
pip install -r requirements.txt
# run the app
python wow-addon-manager info gtfo
```

## Usage and config

Will be added with release v1.0.
