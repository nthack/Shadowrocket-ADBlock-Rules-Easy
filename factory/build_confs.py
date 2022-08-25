# -*- coding: utf-8 -*-

import re
import time


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
