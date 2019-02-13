# WOW Addon Manager

*这是一个**魔兽世界**的**命令行**插件管理工具. 使用Python3.7构建.*

[![Build Status](https://travis-ci.org/qwezarty/wow-addon-manager.svg?branch=master)]( https://travis-ci.org/qwezarty/wow-addon-manager.svg?branch=master)
[![Change Language](https://img.shields.io/badge/README-%20English-yellow.svg)](README.md)

## 开发进度

info && install 在2月12日已经完成！我尽量在三月前发布v1.0版本！

| 任务                       | 状态                             |
|:--------------------------|:--------------------------------:|
| 构架 && 命令行入口          |                            完成！ |
| 用户和系统配置              |                            完成！ |
| 模块：info                 |                            完成！ |
| 模块: install              |                            完成！ |
| 模块: search               |                 进行中，计划2月14日 |
| 模块: update               |                 进行中，计划2月16日 |
| 模块: remove               |                 未开始，计划2月18日 |
| 模块: upgrade              |                 未开始，计划2月21日 |
| 模块: scan                 |                 未开始，计划2月25日 |
| 发布v1.0版本                |                         计划三月前 |

## 重要的碎碎念

建立*wow-addon-manager*项目最初的本意是创建一个**命令行**工具，去替代*Curse Client (它现在和Twich集成在了一起，我非常不喜欢这点)*.

这个项目现在正处于**早期的开发阶段**，现在没有任何的稳定版放出.

如果你是一个*魔兽世界肝帝 & 996的码奴*，我相信你会喜欢使用它.

非常非常希望你能够加入这个项目，去为它提出一些建议或改善代码和细节.

## 将会支持的特性

- 源：curseforge (进行中)，wowinterface (计划中)

- 搜索/详情/安装/更新/移除 插件 (进行中)

- 检查是否已有插件过期，并且能够更新它们 (计划中)

- 本地已经安装的插件检测功能并且全部更新它们 (计划中)

- Windows-10 && macOS 系统将会在1.0版本得到所有的功能支持

## 安装手记

在下载并运行这个项目之前，你需要安装 **Python 3 (with pip)** 和 **Git**

在安装完毕以后，Mac/Linux上你可以运行下面的命令：

``` bash
# 克隆这个仓库
git clone https://github.com/qwezarty/wow-addon-manager.git
# 进入仓库
cd wow-addon-manager
# 安装依赖（Linux可能需要加入'sudo'前缀）
pip install -r requirements.txt
# 运行程序
python wow-addon-manager info gtfo
```

## 使用和配置

将会在v1.0版本发布时，一起附带上。
