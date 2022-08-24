#!/bin/bash

## 构建一系列的规则列表
python3.9 ad.py
python3.9 gfwlist.py
python3.9 build_confs.py
cd ..


## 自动推送
git add .
git commit -m "Daily build" -m "已合并最新的去广告规则及 GFWList"
git push
