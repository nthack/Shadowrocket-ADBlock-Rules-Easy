## 最完善的 iOS 翻墙规则


### 一、前言
由于原作者[h2y](https://github.com/h2y/Shadowrocket-ADBlock-Rules)暂停维护[原项目](https://github.com/h2y/Shadowrocket-ADBlock-Rules)，本项目对原项目进行部分修改，包括文件夹结构、README内容、删除不能使用的规则、修改生成规则等等。

------------------------------------------------------

### 二、规则列表
#### 2.1 列表概述

<table>
    <tr>
        <th>规则简称</th><th>广告</th><th>规则文件名</th><th>代理的网站</th><th>直连的网站</th>
    </tr>
    <tr>
        <td rowspan="2">黑名单</td><td>-</td><td>sr_banlist.conf</td><td rowspan="2">被墙的网站（GFWList）</td><td rowspan="2">1. 已知直连列表<br>2. 正常的网站</td>
    </tr>
    <tr>
        <td>去</td><td>sr_banlist_ad.conf</td>
    </tr>
    <tr>
        <td rowspan="2">黑名单+自定义列表</td><td>-</td><td>sr_banlist_manual.conf</td><td rowspan="2">1. 被墙的网站（GFWList）<br>2. 自定义走代理的列表</td><td rowspan="2">1. 已知直连列表<br>2. 正常的网站<br>3. 自定义直连列表</td>
    </tr>
    <tr>
        <td>去</td><td>sr_banlist_ad_manual.conf</td>
    </tr>
</table>

#### 2.2 自定义列表分为：
	1. 自定义走代理的列表：[manual_proxy]
	2. 自定义走直连的列表：[manual_direct]

------------------------------------------------------

### 脚本环境要求

* beautifulsoup4
* requests
* lxml
