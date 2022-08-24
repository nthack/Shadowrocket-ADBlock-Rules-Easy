# -*- coding: utf-8 -*-

#
# 下载并解析最新版本的 GFWList
# 对于混合性质的网站，尽量走代理（忽略了所有的@@指令）
#


import time
import requests
import re
import base64


rules_url = 'https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt'

unhandle_rules = []


# 获取GFWList并解析
def get_rule(rules_url):

    print('正在加载列表：' + rules_url)

    success = False
    try_times = 0
    r = None
    while try_times < 5 and not success:

        print('尝试次数: ', try_times+1)

        r = requests.get(rules_url)

        if r.status_code != 200:
            time.sleep(1)
            try_times = try_times + 1
        else:
            success = True
            break

    if not success:
        raise Exception('请求失败： %s\n\t 返回HTTP代码为: %d' % (rules_url, r.status_code) )


    print('成功获取GFWList列表，正在转换...')

    time.sleep(1)
    rule = base64.b64decode(r.text) \
            .decode("utf-8") \
            .replace('\\n', '\n')

    return rule


def clear_format(rule):
    rules = []

    rule = rule.split('\n')
    for row in rule:
        row = row.strip()

        # 注释 直接跳过
        if row == '' or row.startswith('!') or row.startswith('@@') or row.startswith('[AutoProxy'):
            continue

        # 清除前缀
        row = re.sub(r'^\|?https?://', '', row)
        row = re.sub(r'^\|\|', '', row)
        row = row.lstrip('.*')

        # 清除后缀
        row = row.rstrip('/^*')

        print('find rule: ', row)

        rules.append(row)

    print('解析GFWList完毕,共找到规则条数：', rules.count)

    return rules


def filtrate_rules(rules):
    ret = []

    for rule in rules:
        rule0 = rule

        # only hostname
        if '/' in rule:
            split_ret = rule.split('/')
            rule = split_ret[0]

        if not re.match('^[\w.-]+$', rule):
            unhandle_rules.append(rule0)
            continue

        ret.append(rule)

    ret = list( set(ret) )
    ret.sort()

    return ret



# main

rule = get_rule(rules_url)

rules = clear_format(rule)

rules = filtrate_rules(rules)

open('resultant/gfw.list', 'w', encoding='utf-8') \
    .write('\n'.join(rules))

open('resultant/gfw_unhandle.log', 'w', encoding='utf-8') \
    .write('\n'.join(unhandle_rules))
