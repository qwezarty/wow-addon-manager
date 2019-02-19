# WOW Addon Manager

*A **cli tool** for maintaining **World of Warcraft** addons. Built with python3.7.*

[![Build Status](https://travis-ci.org/qwezarty/wow-addon-manager.svg?branch=master)](https://travis-ci.org/qwezarty/wow-addon-manager)
[![切换中文](https://img.shields.io/badge/README-切换中文-yellow.svg)](README_zh.md)

## Project status

Sorry for putting off everything by a month! v1.0 will be released at April! 

| Task                      | Status                           |
|:--------------------------|:--------------------------------:|
| scaffolds && cli entrance |                            Done! |
| system && user configs    |                            Done! |
| module: info              |                            Done! |
| module: install           |                            Done! |
| module: search            |                            Done! |
| module: update            |      in-progress, planned 16 Mar |
| module: remove            |      not started, planned 18 Mar |
| module: upgrade           |       not started, planed 21 Mar |
| module: scan              |      not started, planned 25 Mar |
| release v1.0              |                 planned at April |

## Important

The purpose to build *wow-addon-manager* at the very beginning is to make an alternative **cli tool** to *Curse Client (integrate with Twich now, I don't like this)*.

This project is now in **early stage of development**. There's no stable release at all!

Now here is what you want if you're a *wower && developer*.

I'm enthusiastically hope you can join me and make any improvements or suggestions to it.

## Screenshots

![search](https://github.com/qwezarty/wow-addon-manager/raw/master/screenshots/search.png)

![info](https://github.com/qwezarty/wow-addon-manager/raw/master/screenshots/info.png)

![install](https://github.com/qwezarty/wow-addon-manager/raw/master/screenshots/install.png)

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
