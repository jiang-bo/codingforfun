#!/bin/sh
#清理hosts中共用测试环境绑定,需要与获取测试环境绑定脚本共用
#Author:jiangbo
#Date: Mon Jun 25 20:56:34 CST 2012

f_begin=`grep -n '####mark####' /etc/hosts |cut -d: -f1`
f_end=`grep -n '####end####' /etc/hosts|cut -d: -f1`

echo $f_begin,$f_end
sudo cp /etc/hosts /etc/hosts_bak
sudo sed "$f_begin,$f_end""d" /etc/hosts_bak > /etc/hosts
