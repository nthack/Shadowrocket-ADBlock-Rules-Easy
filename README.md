## 最完善的 iOS 翻墙规则

### 项目概览

> 项目中所有的规则每天定时更新：

![](https://img.shields.io/badge/规则更新时间-2022.08.26%2008%3A28%3A03-blue?style=for-the-badge&logo=AdGuard)

![](https://img.shields.io/badge/GFW规则数-5907-critical?style=for-the-badge&logo=SpringSecurity)

![](https://img.shields.io/badge/AdBlock规则数-26756-blueviolet?style=for-the-badge&logo=AdBlock)




<br>
<br>

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
        <td rowspan="2">黑名单</td><td>-</td><td><a href="https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/sr_banlist.conf" target="_blank">sr_banlist.conf</a></td><td rowspan="2">被墙的网站（GFWList）</td><td rowspan="2">1. 已知直连列表<br>2. 正常的网站</td>
    </tr>
    <tr>
        <td>去</td><td><a href="https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/sr_banlist_ad.conf" target="_blank">sr_banlist_ad.conf</a></td>
    </tr>
    <tr>
        <td rowspan="2">黑名单+自定义列表</td><td>-</td><td><a href="https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/sr_banlist_manual.conf" target="_blank" >sr_banlist_manual.conf</a></td><td rowspan="2">1. 被墙的网站（GFWList）<br>2. 自定义走代理的列表</td><td rowspan="2">1. 已知直连列表<br>2. 正常的网站<br>3. 自定义直连列表</td>
    </tr>
    <tr>
        <td>去</td><td><a href="https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/sr_banlist_ad_manual.conf" target="_blank">sr_banlist_ad_manual.conf</a></td>
    </tr>
</table>


<br><br>

#### 2.2 关于自定义列表：

2.2.1 自定义列表文件夹路径：

> [factory/manual/](https://github.com/nthack/Shadowrocket-ADBlock-Rules-Easy/tree/master/factory/manual)


<br>

2.2.2 自定义文件：

- 自定义走代理的列表：[manual_proxy](https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/factory/manual/manual_proxy.txt)
- 自定义走直连的列表：[manual_direct](https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/factory/manual/manual_direct.txt)
- 自定义广告拦截列表：[manual_reject](https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/factory/manual/manual_reject.txt)
- 自定义gfwlist列表（功能与`manual_proxy`一样）：[manual_gfwlist](https://raw.githubusercontent.com/nthack/Shadowrocket-ADBlock-Rules-Easy/master/factory/manual/manual_gfwlist.txt)

------------------------------------------------------



### 脚本环境要求

* beautifulsoup4
* requests
* lxml

