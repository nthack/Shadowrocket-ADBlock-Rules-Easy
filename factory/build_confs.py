# -*- coding: utf-8 -*-

import re
import time
import urllib.parse
import PropFileRW


# 在 template/ 和 ../ 下的文件名称
# except sr_head and sr_foot
confs_names = [
    'sr_banlist',
    'sr_banlist_manual',
    'sr_banlist_ad',
    'sr_banlist_ad_manual'
]


def getRulesStringFromFile(path, kind):
    file = open(path, 'r', encoding='utf-8')
    contents = file.readlines()
    ret = ''

    for content in contents:
        content = content.strip('\r\n')
        if not len(content):
            continue

        if content.startswith('#'):
            ret += content + '\n'
        else:
            prefix = 'DOMAIN-SUFFIX'
            if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', content):
                prefix = 'IP-CIDR'
                if '/' not in content:
                    content += '/32'
            elif '.' not in content:
                prefix = 'DOMAIN-KEYWORD'

            ret += prefix + ',%s,%s\n' % (content, kind)

    return ret


# get head and foot
str_head = open('template/sr_head.txt', 'r', encoding='utf-8').read()
str_foot = open('template/sr_foot.txt', 'r', encoding='utf-8').read()


# make values marks
values = {}

values['build_time'] = time.strftime("%Y-%m-%d %H:%M:%S")

values['top500_proxy']  = getRulesStringFromFile('resultant/top500_proxy.list', 'Proxy')
values['top500_direct'] = getRulesStringFromFile('resultant/top500_direct.list', 'Direct')

values['ad'] = getRulesStringFromFile('resultant/ad.list', 'Reject')

values['manual_direct'] = getRulesStringFromFile('manual/manual_direct.txt', 'Direct')
values['manual_proxy']  = getRulesStringFromFile('manual/manual_proxy.txt', 'Proxy')
values['manual_reject'] = getRulesStringFromFile('manual/manual_reject.txt', 'Reject')

values['gfwlist'] = getRulesStringFromFile('resultant/gfw.list', 'Proxy') \
                  + getRulesStringFromFile('manual/manual_gfwlist.txt', 'Proxy')


# make confs
for conf_name in confs_names:
    print('正在构建ShadowRocket列表：', conf_name)

    file_template = open('template/'+conf_name+'.txt', 'r', encoding='utf-8')
    template = file_template.read()

    template = str_head + template + str_foot

    file_output = open('../'+conf_name+'.conf', 'w', encoding='utf-8')


    # marks：在模板文件里面定义的"{{xxx}}"，但是也要和上面values定义的对应上
    # 与文件名称无关
    marks = re.findall(r'{{(.+)}}', template)


    for mark in marks:
        print('包含列表：', mark)
        template = template.replace('{{'+mark+'}}', values[mark])

    file_output.write(template)

    print('ShadowRocket列表：', conf_name,' 构建完成\n\n')



# 自动更新README.md
# Auto Update README.md when executing this file
readme_file_template = open('template/README_template.txt', 'r', encoding='utf-8')
readme_template = readme_file_template.read()
readme_marks = re.findall(r'{{(.+)}}', readme_template)

# 读取repo_status.prop文件
adblocklistlength = PropFileRW.readProp('adblocklistlength')
gfwlistlength = PropFileRW.readProp('gfwlistlength')


# Silly String format
timecode = time.strftime('%Y.%m.%d %H:%M:%S')
timecode = urllib.parse.quote(timecode)
update_badge="![](https://img.shields.io/badge/规则更新时间-" + timecode + "-blue?style=for-the-badge&logo=AdGuard)"
GFWlistBadge="![](https://img.shields.io/badge/GFW规则数-" + gfwlistlength + "-critical?style=for-the-badge&logo=SpringSecurity)"
adBlockBadge="![](https://img.shields.io/badge/AdBlock规则数-" + adblocklistlength + "-blueviolet?style=for-the-badge&logo=AdBlock)"


# Data Declare
readme_data = {}
readme_data['updateTimeBadge'] = update_badge
readme_data['GFWlistBadge'] = GFWlistBadge
readme_data['adBlockBadge'] = adBlockBadge



for mark in readme_marks:
    print('替换README数据', mark)
    readme_template = readme_template.replace('{{'+mark+'}}', readme_data[mark])


readme_file_output = open('../README.md', 'w', encoding='utf-8')
readme_file_output.write(readme_template)