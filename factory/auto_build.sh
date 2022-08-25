#!/bin/bash

## 构建一系列的规则列表
python3 ad.py
python3 gfwlist.py
python3 build_confs.py


cd ..
git add .
git commit -m 'Daily Build' -m '更新GFWList及所有规则'
git push