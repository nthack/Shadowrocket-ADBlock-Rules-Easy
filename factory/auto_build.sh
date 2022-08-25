#!/bin/bash

Path=./factory
cd $Path

## 构建一系列的规则列表
python3 ad.py
python3 gfwlist.py
python3 build_confs.py