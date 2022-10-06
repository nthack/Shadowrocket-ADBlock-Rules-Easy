## 最完善的 iOS 翻墙规则

### 项目概览

> 项目中所有的规则每天定时更新：

![](https://img.shields.io/badge/规则更新时间-2022.10.06%2009%3A59%3A05-blue?style=for-the-badge&logo=AdGuard)

![](https://img.shields.io/badge/GFW规则数-5914-critical?style=for-the-badge&logo=SpringSecurity)

![](https://img.shields.io/badge/AdBlock规则数-29039-blueviolet?style=for-the-badge&logo=AdBlock)




<br>

![](https://nthack.github.io/nthack/assets/img/Shadowrocket_banner_resize.jpg)

<br>
Repository Page Views Counter

![](https://komarev.com/ghpvc/?username=nthack-shadowrocket-rules&style=for-the-badge&color=dc143c&label=Repository+Views)

<br>
<br>

### 一、前言
由于原作者[h2y](https://github.com/h2y/Shadowrocket-ADBlock-Rules)暂停维护[原项目](https://github.com/h2y/Shadowrocket-ADBlock-Rules)，本项目对原项目进行部分修改，包括文件夹结构、README内容、删除不能使用的规则、修改生成规则等等。

<br>

### 二、请保护好自己

谷歌中英文的搜索体验都优于百度，而刷美剧、ins 追星、去推特看看特朗普也都挺有意思。但是，随着看到的人和事越多，我越发想要在这里说一些话，告诫路过的各位：

**请务必保护好自己** 我们自认为打破了信息的壁垒，其实打破的是保护我们的屏障。因为外网真的存在很多误导性言论，来自各个利益集团对中国网民疯狂洗脑，他们往往还喜欢以平等自由等旗号自称，但仔细想想真的是这样吗？我只知道美国是最善于运用舆论的国家，会结合大数据潜移默化地改变你的观念。如果大家在上网过程中不经意看到了某些观点，务必保留自己独立思考的能力，如果你是一个容易被带偏的人，则建议回到屏障之中。

本规则只提供给大家用于更便捷地学习和工作。如果你是对上述观点持反对意见的极端政治人士，或者已被洗脑，请立即离开，本项目不对你开放。


------------------------------------------------------

### 三、规则列表
#### 2.1 列表概述

<table>
    <tr>
        <th>规则简称</th><th>广告</th><th>规则文件名</th><th>代理的网站</th><th>直连的网站</th>
    </tr>
    <tr>
        <td rowspan="2">黑名单</td><td>-</td><td><a href="https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/sr_banlist.conf" target="_blank">sr_banlist.conf</a></td><td rowspan="2">被墙的网站（GFWList）</td><td rowspan="2">1. 已知直连列表<br>2. 正常的网站</td>
    </tr>
    <tr>
        <td>去</td><td><a href="https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/sr_banlist_ad.conf" target="_blank">sr_banlist_ad.conf</a></td>
    </tr>
    <tr>
        <td rowspan="2">黑名单+自定义列表</td><td>-</td><td><a href="https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/sr_banlist_manual.conf" target="_blank" >sr_banlist_manual.conf</a></td><td rowspan="2">1. 被墙的网站（GFWList）<br>2. 自定义走代理的列表</td><td rowspan="2">1. 已知直连列表<br>2. 正常的网站<br>3. 自定义直连列表</td>
    </tr>
    <tr>
        <td>去</td><td><a href="https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/sr_banlist_ad_manual.conf" target="_blank">sr_banlist_ad_manual.conf</a></td>
    </tr>
</table>


<br><br>

#### 2.2 关于自定义列表：

2.2.1 自定义列表文件夹路径：

> [factory/manual/](https://github.com/nthack/Shadowrocket-ADBlock-Rules-Easy/tree/master/factory/manual)


<br>

2.2.2 自定义文件：

- 自定义走代理的列表：[manual_proxy](https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/factory/manual/manual_proxy.txt)
- 自定义走直连的列表：[manual_direct](https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/factory/manual/manual_direct.txt)
- 自定义广告拦截列表：[manual_reject](https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/factory/manual/manual_reject.txt)
- 自定义gfwlist列表（功能与`manual_proxy`一样）：[manual_gfwlist](https://nthack.github.io/Shadowrocket-ADBlock-Rules-Easy/factory/manual/manual_gfwlist.txt)

------------------------------------------------------



### 脚本环境要求

* beautifulsoup4
* requests
* lxml

