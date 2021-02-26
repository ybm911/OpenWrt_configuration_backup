# OpenWrt configuration backup

OpenWrt 自动下载设置备份（不是系统备份），并清理30天前下载的备份

![OpenWrt](https://cdn.jsdelivr.net/gh/ybm911/blog_picture/img/20210226104230.png)

由于 OpenWrt 刷入软路由的不稳定性，每次重启有几率无法联网，以及软路由有时不时自动关机的毛病（时间可能为一个月自动关机一次），故此项目就诞生了。

## Features

* 登陆软路由，下载位于：系统 -> 备份/升级 -> 动作 -> 备份/恢复 的下载备份
* 每隔一天在7点执行一次下载备份
* 自动删除2个月前的备份（即只允许保留30个备份）

## 使用

### 安装

需要 Python 模块

```
requests
re
sys
bs4
pyyaml
```

`sudo python3 -m pip install -r requirements.txt`

### 配置

配置文件 `config.yaml` 填写

```yaml
---
# OpenWrt 的 ip (ipv4)，例子：192.168.3.1:80
ip : ""
# 登陆的用户名
username : ""
# 登陆的密码
password : ""
```

### 运行

`sudo sh task.sh`



**仅固件版本为：OpenWrt R20.6.18 / LuCI Master (git-20.117.60969-420c61a) 的被验证过**